from pkg_resources import resource_filename

Gaussian_default = {'xyz_file': resource_filename(__name__,
                                                  'gaussian/default_settings/propane.xyz'),
                    'out_file': resource_filename(__name__,
                                                  'gaussian/default_settings/propane_qforce/propane_hessian.log'),
                    'fchk_file': resource_filename(__name__,
                                                   'gaussian/default_settings/propane_qforce/propane_hessian.fchk'),
                    'fragments': resource_filename(__name__,
                                              'gaussian/default_settings/propane_qforce/fragments/CC_H8C3_d91b46644317dee9c2b868166c66a18c~1.log')}

Orca_default = {'xyz_file': resource_filename(__name__,
                                                  'orca/default_settings/propane.xyz'),
                'out_file': resource_filename(__name__,
                                                  'orca/default_settings/propane_qforce/propane_hessian.log'),
                'hess_file': resource_filename(__name__,
                                                  'orca/default_settings/propane_qforce/propane_opt.hess'),
                'pc_file': resource_filename(__name__,
                                                  'orca/default_settings/propane_qforce/propane_charge.pc_chelpg'),
                'coord_file': resource_filename(__name__,
                                                  'orca/default_settings/propane_qforce/propane_opt.xyz'),
                'fragments' : resource_filename(__name__,
                                                  'orca/default_settings/propane_qforce/fragments/CC_H8C3_d91b46644317dee9c2b868166c66a18c~2.log')}