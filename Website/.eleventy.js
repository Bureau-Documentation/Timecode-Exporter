const { DateTime } = require("luxon");
const CleanCSS = require("clean-css");
const htmlmin = require("html-minifier");
const markdownIt = require("markdown-it");
const markdownItAttrs = require("markdown-it-attrs");
const markdownItAnchor = require("markdown-it-anchor");

module.exports = function(eleventyConfig) {

    eleventyConfig.setUseGitIgnore(false);

    const mdOptions = {
        html: true,
        breaks: true,
        linkify: true,
    };

    const markdownItAnchorOptions = {
      level: 2, // minimum level header -- anchors will only be applied to h2 level headers and below but not h1
      permalink: true,
    }

    const markdownLib = markdownIt(mdOptions)
        .use(markdownItAnchor,markdownItAnchorOptions)
        .use(markdownItAttrs)
        .use(require('markdown-it-bracketed-spans'))
        .disable("code");

    eleventyConfig.setLibrary("md", markdownLib);

    eleventyConfig.setTemplateFormats([
        "md",
        "webmanifest",
        "xml",
        "ico",
        "svg",
        "png",
        "jpg",
        "txt",
        "woff",
        "woff2",
        "css",
        "pdf"
      ]);

    eleventyConfig.addFilter("readablePostDate", (dateObj) => {
        return DateTime.fromJSDate(dateObj, {
            zone: "Asia/Singapore",
        }).setLocale('en-GB').toLocaleString({day: 'numeric',month: 'short',year: 'numeric'});
    });

    eleventyConfig.addFilter("postDate", (dateObj) => {
        return DateTime.fromJSDate(dateObj, {
            zone: "Asia/Singapore",
        }).setLocale('en-GB').toISODate();
    });

    eleventyConfig.addTransform("htmlmin", function(content, outputPath) {
        if( outputPath && outputPath.endsWith(".html") ) {
            let minified = htmlmin.minify(content, {
                useShortDoctype: true,
                removeComments: true,
                collapseWhitespace: true
            });
        return minified;
        }
    return content;
    });

    return {
        dir: {
        input: "src",
        includes: "_includes",
        output: "site"
        }
    }

    eleventyConfig.addPassthroughCopy('/src/css')
      return {
        passthroughFileCopy: true
      }
};
