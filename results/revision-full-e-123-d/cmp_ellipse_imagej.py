"""
Compare Ellipse and ImageJ results.

Parameters: output_dir
"""
import dist_mixtures.mixture_von_mises as mvm

output_dir = 'output/ellipse-lengths'
output_dir = 'output/imagej'
output_dir = 'output/area-angles'
output_dir = 'output/tmp'
output_dir = 'output/full-e-123-d'
output_dir = 'output/full-e-45-d'
output_dir = 'output/revision-full-e-123-d'

def callback(x, f, accept):
    print accept, '%20.12f' % f

parameter_sets = [
    {
        'model_class' : mvm.VonMisesMixtureBinned,
        'n_components' : 1,
        'parameters' : [2.0, 0.0], # Starting values.
        'solver' : ('basinhopping', {
            'T' : 0.001, 'stepsize' : 0.2, 'callback' : callback,
            'niter' : 200, 'niter_success' : 100,
            'minimizer' : {
                'method' : 'L-BFGS-B',
                'tol' : 1e-9,
            }
        }),
        'output_dir' : output_dir,
    },
    {
        'n_components' : 2,
    },
    {
        'n_components' : 3,
    },
    ## {
    ##     'n_components' : 4,
    ## },
    ## {
    ##     'n_components' : 5,
    ## },
]
