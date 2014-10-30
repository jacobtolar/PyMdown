import bleach

tags = [
    'a', 'abbr', 'acronym', 'address', 'area', 'b', 'big',
    'blockquote', 'br', 'button', 'caption', 'center', 'cite', 'code', 'col',
    'colgroup', 'dd', 'del', 'dfn', 'dir', 'div', 'dl', 'dt', 'em',
    'font', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'hr', 'i', 'img',
    'ins', 'kbd', 'label', 'legend', 'li', 'map', 'menu', 'ol',
    'p', 'pre', 'q', 's', 'samp', 'small', 'span', 'strike',
    'strong', 'sub', 'sup', 'table', 'tbody', 'td', 'tfoot', 'th',
    'thead', 'tr', 'tt', 'u', 'ul', 'var'
]

attrs = [
    'abbr', 'accept', 'accept-charset', 'accesskey',
    'action', 'align', 'alt', 'aria-hidden', 'axis', 'border', 'cellpadding', 'cellspacing',
    'char', 'charoff', 'charset', 'checked', 'cite', 'class', 'clear', 'cols',
    'colspan', 'color', 'compact', 'coords', 'datetime', 'dir',
    'enctype', 'for', 'headers', 'height', 'href', 'hreflang', 'hspace',
    'id', 'ismap', 'label', 'lang', 'longdesc', 'maxlength', 'method',
    'multiple', 'name', 'nohref', 'noshade', 'nowrap', 'prompt',
    'rel', 'rev', 'rows', 'rowspan', 'rules', 'scope', 'shape', 'size', 'style',
    'span', 'src', 'start', 'summary', 'tabindex', 'target', 'title', 'type',
    'usemap', 'valign', 'value', 'vspace', 'width'
]

styles = [
    "-moz-border-radius-bottomleft", "-moz-border-radius-bottomright", "-moz-border-radius-topleft",
    "-moz-border-radius-topright", "animation", "animation-delay", "animation-direction",
    "animation-duration", "animation-fill-mode", "animation-iteration-count", "animation-name",
    "animation-play-state", "animation-timing-function", "appearance", "azimuth", "backface-visibility",
    "background", "background-attachment", "background-color", "background-image", "background-position",
    "background-repeat", "background-size", "border", "border-bottom", "border-bottom-color",
    "border-bottom-left-radius", "border-bottom-right-radius", "border-bottom-style", "border-bottom-width",
    "border-collapse", "border-color", "border-left", "border-left-color", "border-left-style", "border-left-width",
    "border-radius", "border-right", "border-right-color", "border-right-style", "border-right-width",
    "border-spacing", "border-style", "border-top", "border-top-color", "border-top-left-radius",
    "border-top-right-radius", "border-top-style", "border-top-width", "border-width", "bottom", "box",
    "box-shadow", "box-sizing", "caption-side", "clear", "clip", "color", "content", "cue", "cue-after",
    "cue-before", "cursor", "direction", "display", "display-extras", "display-inside", "display-outside",
    "elevation", "empty-cells", "filter", "float", "font", "font-family", "font-size", "font-stretch", "font-style",
    "font-variant", "font-weight", "height", "left", "letter-spacing", "line-height", "list-style", "list-style-image",
    "list-style-position", "list-style-type", "margin", "margin-bottom", "margin-left", "margin-right", "margin-top",
    "max-height", "max-width", "min-height", "min-width", "opacity", "outline", "outline-color", "outline-style",
    "outline-width", "overflow", "overflow-wrap", "overflow-x", "overflow-y", "padding", "padding-bottom",
    "padding-left", "padding-right", "padding-top", "page-break-after", "page-break-before", "page-break-inside",
    "pause", "pause-after", "pause-before", "perspective", "perspective-origin", "pitch", "pitch-range",
    "play-during", "position", "quotes", "resize", "richness", "right", "speak", "speak-header", "speak-numeral",
    "speak-punctuation", "speech-rate", "stress", "table-layout", "text-align", "text-decoration", "text-indent",
    "text-overflow", "text-shadow", "text-transform", "text-wrap", "top", "transform", "transform-origin",
    "transform-style", "transition", "transition-delay", "transition-duration", "transition-property",
    "transition-timing-function", "unicode-bidi", "vertical-align", "visibility", "voice-family", "volume",
    "white-space", "widows", "width", "word-break", "word-spacing", "word-wrap", "z-index" "zoom"
]


def scrub(content):
    return bleach.clean(content, tags, attrs, styles, strip=True, strip_comments=False)
