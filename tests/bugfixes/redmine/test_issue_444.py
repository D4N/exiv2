# -*- coding: utf-8 -*-

import system_tests


class PanicOnMisinformedIPTC(system_tests.Case):
    """
    TODO: there is currently an encoding problem with the character Ä
    in the first line of stdout. exiv2 does not output it as correctly
    encoded utf-8 => Python fails to decode it with utf-8 and the
    whole thing fails miserably
    """

    url = "http://dev.exiv2.org/issues/444"

    filename = "{data_path}/exiv2-bug444.jpg"
    commands = ["{exiv2} -u -pi " + filename]
    stdout = ["""Iptc.Envelope.CharacterSet                   String      4  Ä
Iptc.Application2.Urgency                    String      2  GT
Iptc.Application2.SuppCategory               String      8  portrait
Iptc.Application2.Caption                    String     18  Witty caption here
Iptc.Application2.Keywords                   String      3  ize
Iptc.Application2.0x007b                     String      4  n123
"""]
    stderr = [""]
    retval = [0]
