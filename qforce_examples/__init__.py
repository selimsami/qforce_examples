"""Example and test files for Qforce."""

# Add imports here
from pkg_resources import resource_filename

Gaussian_default = {'xyz_file': resource_filename(__name__,
                                                  'gaussian/default_settings/propane.xyz'),
                    'out_file': resource_filename(__name__,
                                                  'gaussian/default_settings/necessary_files/propane_hessian.out'),
                    'fchk_file': resource_filename(__name__,
                                                   'gaussian/default_settings/necessary_files/propane_hessian.fchk'),
                    'fragments': resource_filename(__name__,
                                                   'gaussian/default_settings/necessary_files/fragments/CC_H8C3_d91b46644317dee9c2b868166c66a18c~1.out')}

Orca_default = {'xyz_file': resource_filename(__name__,
                                                  'orca/default_settings/propane.xyz'),
                'out_file': resource_filename(__name__,
                                                  'orca/default_settings/necessary_files/propane_hessian.out'),
                'hess_file': resource_filename(__name__,
                                                  'orca/default_settings/necessary_files/propane_opt.hess'),
                'pc_file': resource_filename(__name__,
                                                  'orca/default_settings/necessary_files/propane_charge.pc_chelpg'),
                'coord_file': resource_filename(__name__,
                                                  'orca/default_settings/necessary_files/propane_opt.xyz'),
                'fragments_out' : resource_filename(__name__,
                                                  'orca/default_settings/necessary_files/fragments/CC_H8C3_d91b46644317dee9c2b868166c66a18c~1.out'),
                'fragments_pc' : resource_filename(__name__,
                                                  'orca/default_settings/necessary_files/fragments/CC_H8C3_d91b46644317dee9c2b868166c66a18c~1_charge.pc_chelpg'),
                'fragments_coord' : resource_filename(__name__,
                                                  'orca/default_settings/necessary_files/fragments/CC_H8C3_d91b46644317dee9c2b868166c66a18c~1_scan.allxyz'),
                'fragments_angle' : resource_filename(__name__,
                                                  'orca/default_settings/necessary_files/fragments/CC_H8C3_d91b46644317dee9c2b868166c66a18c~1_scan.relaxscanact.dat'),
                'fragments_sp': resource_filename(__name__,
                                                  'orca/default_settings/necessary_files/fragments/CC_H8C3_d91b46644317dee9c2b868166c66a18c~1_sp.xyzact.dat'),
                }

Gaussian_DMF = {'xyz_file': resource_filename(__name__,
                                              'gaussian/DMF/DMF.xyz'),
                'out_file': resource_filename(__name__,
                                              'gaussian/DMF/necessary_files/DMF_hessian.log'),
                'fchk_file': resource_filename(__name__,
                                               'gaussian/DMF/necessary_files/DMF_hessian.fchk'),}

ORCA_DMF = {'xyz_file': resource_filename(__name__, 'orca/DMF/DMF.xyz'),
            'out_file': resource_filename(__name__,
                                          'orca/DMF/necessary_files/DMF_hessian.out'),
            'hess_file': resource_filename(__name__,
                                           'orca/DMF/necessary_files/DMF_opt.hess'),
            'pc_file': resource_filename(__name__,
                                         'orca/DMF/necessary_files/DMF_charge.pc_chelpg'),
            'coord_file': resource_filename(__name__,
                                            'orca/DMF/necessary_files/DMF_opt.xyz'),
            }