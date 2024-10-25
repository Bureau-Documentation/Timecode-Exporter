package main

import (
  "bufio"
  "fmt"
  "os"
  "strconv"
  "strings"

  "fyne.io/fyne/v2"
  "fyne.io/fyne/v2/app"
  "fyne.io/fyne/v2/container"
  "fyne.io/fyne/v2/dialog"
  "fyne.io/fyne/v2/layout"
  "fyne.io/fyne/v2/widget"
  "github.com/atotto/clipboard"
)

type TextAlign int

const (
  TextAlignLeading TextAlign = iota
  TextAlignCenter
  TextAlignTrailing
)

func main() {
  os.Setenv("LANG", "en_US.UTF-8")
  os.Setenv("LC_ALL", "en_US.UTF-8")

  a := app.New()
  w := a.NewWindow("Timecode Exporter")
  w.Resize(fyne.NewSize(500, 500))

  instructionsLabel := widget.NewLabel("Drag and drop the .edl file here")
  content := container.New(layout.NewCenterLayout(), instructionsLabel)

  w.SetOnDropped(func(pos fyne.Position, uris []fyne.URI) {
    for _, uri := range uris {
      if err := processFile(uri.Path(), w); err != nil {
        dialog.NewError(err, w).Show()
      }
    }
  })

  w.SetContent(content)
  w.ShowAndRun()
}

func processFile(filePath string, w fyne.Window) error {
  file, err := os.Open(filePath)
  if err != nil {
    return fmt.Errorf("could not open file: %v", err)
  }
  defer file.Close()

  var timeRanges []string
  scanner := bufio.NewScanner(file)

  for scanner.Scan() {
    line := scanner.Text()
    columns := strings.Fields(line)

    if len(columns) > 7 && isNumeric(columns[0]) {
      startTime := columns[6][:8]
      endTime := columns[7][:8]
      timeRanges = append(timeRanges, fmt.Sprintf("%s to %s", startTime, endTime))
    }
  }

  if err := scanner.Err(); err != nil {
    return fmt.Errorf("error reading file: %v", err)
  }

  if len(timeRanges) == 0 {
    dialog.ShowInformation("No Timecodes", "No valid timecodes found in the file.", w)
    return nil
  }

  formattedTimeRangesForClipboard := strings.Join(timeRanges, "\n\n")

  if err := clipboard.WriteAll(formattedTimeRangesForClipboard); err != nil {
    return fmt.Errorf("could not copy to clipboard: %v", err)
  }

  clipboardMessage := widget.NewLabel("Timecodes are copied to your clipboard. Double check them!")
  okButton := widget.NewButton("OK", func() {
    w.Close()
  })
  okButton.Importance = widget.HighImportance

  formattedTimeRanges := strings.Join(timeRanges, "\n")
  columnOne, columnTwo := splitIntoColumns(formattedTimeRanges)

  columnOneLabel := labelWithAlignment(columnOne, TextAlignCenter)
  columnTwoLabel := labelWithAlignment(columnTwo, TextAlignCenter)

  twoColumnContainer := container.New(layout.NewGridLayout(2), columnOneLabel, columnTwoLabel)

  contentBox := container.NewVBox(clipboardMessage, okButton, twoColumnContainer)
  w.SetContent(contentBox)

  w.Canvas().SetOnTypedKey(func(k *fyne.KeyEvent) {
    w.Close()
  })

  return nil
}

func isNumeric(s string) bool {
  _, err := strconv.Atoi(s)
  return err == nil
}

func labelWithAlignment(text string, align TextAlign) *widget.Label {
  label := widget.NewLabel(text)
  switch align {
  case TextAlignCenter:
    label.Alignment = fyne.TextAlignCenter // Align center if using Fyne's built-in alignment
  case TextAlignLeading:
    label.Alignment = fyne.TextAlignLeading
  case TextAlignTrailing:
    label.Alignment = fyne.TextAlignTrailing
  }
  return label
}

func splitIntoColumns(formattedTimeRanges string) (string, string) {
  lines := strings.Split(formattedTimeRanges, "\n")
  var columnOne, columnTwo []string

  for i, line := range lines {
    if i%2 == 0 {
      columnOne = append(columnOne, line)
    } else {
      columnTwo = append(columnTwo, line)
    }
  }

  return strings.Join(columnOne, "\n"), strings.Join(columnTwo, "\n")
}
