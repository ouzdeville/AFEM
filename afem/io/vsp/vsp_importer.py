from .methods.import_vsp_step import import_vsp_step

__all__ = ["ImportVSP"]


class ImportVSP(object):
    """
    Import a VSP file.
    """
    _bodies = {}

    @classmethod
    def step_file(cls, fn, divide_closed=True):
        """
        Import a STEP file generated by VSP3 (including metadata).

        :param str fn:
        :param divide_closed:

        :return:
        """
        bodies = import_vsp_step(fn, divide_closed)
        cls._bodies.update(bodies)
        return True

    @classmethod
    def clear(cls):
        """
        Clear imported data.
        """
        cls._bodies.clear()
        return True

    @classmethod
    def get_body(cls, name):
        """
        Return OML body by name.

        :param str name: Body name.
        :return: OML body.
        """
        try:
            return cls._bodies[name]
        except KeyError:
            return None

    @classmethod
    def get_bodies(cls):
        """
        Return all bodies in a dictionary.

        :return:
        """
        return cls._bodies
