test = {   'name': 'q5d',
    'points': 3,
    'suites': [   {   'cases': [   {   'code': ">>> tips_with_poly_features.shape == (244, 10) and set(tips_with_poly_features.columns) >= set(['total_bill', 'total_bill^2', 'total_bill^3', "
                                               "'total_bill^4'])\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {'code': '>>> isinstance(X_poly, np.ndarray) and X_poly.shape == (244, 5)\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> isinstance(w_poly, np.ndarray) and w_poly.shape == (5,)\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> isinstance(mse_poly, float) and mse_poly < 1\nTrue', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
