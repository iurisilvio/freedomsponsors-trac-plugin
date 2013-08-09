from genshi.builder import tag
from trac.core import Component, implements
from trac.web.api import IRequestFilter
from trac.web.chrome import add_ctxtnav

class FreedomSponsorsPlugin(Component):

    implements(IRequestFilter)

    def pre_process_request(self, req, handler):
        return handler

    def post_process_request(self, req, template, data, content_type):
        ticket_id = req.args.get('id')
        if template == 'ticket.html' and ticket_id:
            ticket_url = req.abs_href('ticket', ticket_id)
            fs_url = u'http://www.freedomsponsors.org/core/issue/sponsor?trackerURL=%s' % ticket_url
            text = u'Sponsor #%s in FreedomSponsors.org!' % ticket_id
            add_ctxtnav(req, tag.a(text, href=fs_url, target='_blank'))
        return template, data, content_type
