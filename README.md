# Timecode Exporter

An utility to export timecodes from a Sequence in Premiere or a Timeline in DaVinci Resolve.

## Setting up the project

```
go mod init Bureau-Documentation/Timecode-Exporter
export PATH=$PATH:$HOME/go/bin
go install github.com/fyne-io/fyne-cross@latest
GOOS=darwin GOARCH=amd64,arm64 CGO_ENABLED=1
go mod tidy
go clean -modcache
```

## Compiling
```
fyne-cross windows -app-id Timecode.Exporter -no-cache -name "Timecode Exporter" -app-version 2.0.0 -icon ./Icon/Icon.icns -arch=amd64

fyne-cross darwin -app-id Timecode.Exporter -no-cache -name "Timecode Exporter" -app-version 2.0.0 -icon ./Icon/Icon.icns -arch=arm64,amd64
```