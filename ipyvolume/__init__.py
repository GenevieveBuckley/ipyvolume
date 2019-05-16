from __future__ import absolute_import

from ipyvolume._version import __version__  # noqa: F401
from ipyvolume import styles  # noqa: F401
from ipyvolume import examples  # noqa: F401
from ipyvolume import datasets  # noqa: F401
from ipyvolume import embed  # noqa: F401
from ipyvolume.widgets import (Mesh,
                               Scatter,
                               Volume,
                               Figure,
                               quickquiver,
                               quickscatter,
                               quickvolshow,
                               )  # noqa: F401
from ipyvolume.transferfunction import (TransferFunction,
                                        TransferFunctionJsBumps,
                                        TransferFunctionWidgetJs3,
                                        TransferFunctionWidget3,
                                        )  # noqa: F401
from ipyvolume.pylab import (current,
                             clear,
                             controls_light,
                             figure,
                             gcf,
                             xlim,
                             ylim,
                             zlim,
                             xyzlim,
                             squarelim,
                             plot_trisurf,
                             plot_surface,
                             plot_wireframe,
                             plot_mesh,
                             plot,
                             scatter,
                             quiver,
                             show,
                             animate_glyphs,
                             animation_control,
                             gcc,
                             transfer_function,
                             plot_isosurface,
                             volshow,
                             save,
                             movie,
                             screenshot,
                             savefig,
                             xlabel,
                             ylabel,
                             zlabel,
                             xyzlabel,
                             view,
                             style,
                             plot_plane,
                             selector_default,
                             )  # noqa: F401


def _jupyter_nbextension_paths():
    return [
        {
            "section": "notebook",
            "src": "static",
            "dest": "ipyvolume",
            "require": "ipyvolume/extension",
        }
    ]
