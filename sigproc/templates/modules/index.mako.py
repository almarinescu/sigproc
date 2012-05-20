# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 8
_modified_time = 1337355058.5333309
_enable_loop = True
_template_filename = 'sigproc/templates/index.mako'
_template_uri = 'index.mako'
_source_encoding = 'ascii'
_exports = ['head_tags']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'master.mako', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n\n')
        # SOURCE LINE 10
        __M_writer(u'\n\n<div class="body-container">\n  <div class="graph-container main-container">\n    <div class="header-control-container">\n      <div class="header-container">\n        <h3 class="graph-header">Frequency response</h3>\n      </div>\n      <div class="slider-container">\n        <input id="freq-slider" type="slider" name="freq" value="0.1;0.9"/>\n        <div id="graph-overview"></div>\n      </div>\n    </div>\n\n    <div id="freq-resp-graph" class="response-graph"></div>\n  </div>\n\n  <div class="graph-container secondary-container">\n    <h3 class="graph-header">Step response</h3>\n    <div id="step-resp-graph" class="response-graph"></div>\n  </div>\n\n  <div class="graph-container secondary-container">\n    <h3 class="graph-header">Impulse response</h3>\n    <div id="impulse-resp-graph" class="response-graph"></div>\n  </div>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_head_tags(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\n\t<link type="text/css" rel="stylesheet/less" href="/static/css/main.less"/>\n\t<link type="text/css" rel="stylesheet" href="/static/css/jquery.slider.min.css"/>\n  <script type="text/javascript" src="/static/js/jquery-1.7.2.min.js"></script>\n  <script type="text/javascript" src="/static/js/jquery.slider.min.js"></script>\n  <script src="/static/js/flot/jquery.flot.js" type="text/javascript"></script>\n  <script type="text/javascript" src="/static/js/main.js"></script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


