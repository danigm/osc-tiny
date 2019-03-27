"""
Projects extension
------------------
"""
from urllib.parse import urljoin

from .base import ExtensionBase


class Project(ExtensionBase):
    base_path = "/source"

    def get_list(self, deleted=False):
        """
        Get list of projects

        :param deleted: show deleted projects instead of existing
        :type deleted: bool
        :return: Objectified XML element
        :rtype: lxml.objectify.ObjectifiedElement
        """
        deleted = '1' if deleted else '0'
        response = self.osc.request(
            url=urljoin(self.osc.url, self.base_path),
            method="GET",
            data={'deleted': deleted}
        )

        return self.osc.get_objectified_xml(response)

    def get_meta(self, project):
        """
        Get project metadata

        :param project: name of project
        :return: Objectified XML element
        :rtype: lxml.objectify.ObjectifiedElement
        """
        response = self.osc.request(
            url=urljoin(
                self.osc.url,
                "{}/{}/_meta".format(self.base_path, project)
            ),
            method="GET"
        )

        return self.osc.get_objectified_xml(response)

    def get_files(self, project, meta=False, rev=None):
        """
        List project files

        :param project: name of project
        :param meta: switch for _meta files
        :type meta: bool
        :param rev: revision
        :type rev: int
        :return: Objectified XML element
        :rtype: lxml.objectify.ObjectifiedElement
        """
        data = {}
        if meta:
            data["meta"] = '1'
        if rev:
            data["rev"] = str(rev)
        response = self.osc.request(
            url=urljoin(
                self.osc.url,
                "{}/{}/_project".format(self.base_path, project)
            ),
            method="GET",
            data=data
        )

        return self.osc.get_objectified_xml(response)

    def get_attribute(self, project, attribute=None):
        """
        Get one attribute of a project

        :param project: name of project
        :param attribute: name of attribute
        :return: Objectified XML element
        :rtype: lxml.objectify.ObjectifiedElement
        """
        url = urljoin(
            self.osc.url,
            "{}/{}/_attribute".format(
                self.base_path, project
            )
        )

        if attribute:
            url = "{}/{}".format(url, attribute)

        response = self.osc.request(url=url, method="GET")

        return self.osc.get_objectified_xml(response)
