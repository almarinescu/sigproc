# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 8
_modified_time = 1337331649.2645459
_enable_loop = True
_template_filename = u'sigproc/templates/master.mako'
_template_uri = u'master.mako'
_source_encoding = 'ascii'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        self = context.get('self', UNDEFINED)
        title = context.get('title', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<html>\n\t<head>\n\t\t<title>')
        # SOURCE LINE 3
        __M_writer(unicode(title))
        __M_writer(u'</title>\n\t\t')
        # SOURCE LINE 4
        __M_writer(unicode(self.head_tags()))
        __M_writer(u'\n\t\t<script src="/static/js/less.js" type="text/javascript"></script>\n\t</head>\n\t<body>\n\t\t')
        # SOURCE LINE 8
        __M_writer(unicode(self.body()))
        __M_writer(u'\n\t</body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


