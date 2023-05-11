
init python in exp_core:

    class ExPPaths(object):
        """
        This class handles setting paths to ExPoser def files.
        """
        def __init__(self, basedir):
            self.basedir = basedir
            self.clothes = basedir + "/clothes"
            self.eyebrows = basedir + "/eyebrows"
            self.noses = basedir + "/noses"
            self.mouth = basedir + "/mouth"
            self.eyebrows = basedir + "/eyebrows"
            self.eyes = basedir + "/eyes"
            self.blinking = basedir + "/blinking"