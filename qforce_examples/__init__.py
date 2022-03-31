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


Orca_default_NBO6 = {'xyz_file': resource_filename(__name__,
                                                  'orca/default_settings_NBO6/propane.xyz'),
                'out_file': resource_filename(__name__,
                                                  'orca/default_settings_NBO6/necessary_files/propane_hessian.log'),
                'hess_file': resource_filename(__name__,
                                                  'orca/default_settings_NBO6/necessary_files/propane_opt.hess'),
                'pc_file': resource_filename(__name__,
                                                  'orca/default_settings_NBO6/necessary_files/propane_charge.pc_chelpg'),
                'coord_file': resource_filename(__name__,
                                                  'orca/default_settings_NBO6/necessary_files/propane_opt.xyz'),
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

xTB_default = {'xyz_file': resource_filename(__name__,
                                                  'xtb/default_settings/propane.xyz'),
                'wbo_file': resource_filename(__name__,
                                                  'xtb/default_settings/necessary_files/propane_hessian.wbo'),
                'hess_file': resource_filename(__name__,
                                                  'xtb/default_settings/necessary_files/propane_hessian.hessian'),
                'pc_file': resource_filename(__name__,
                                                  'xtb/default_settings/necessary_files/propane_hessian.charges'),
                'coord_file': resource_filename(__name__,
                                                  'xtb/default_settings/necessary_files/propane_hessian.xtbopt.xyz'),
                'fragments_pc' : resource_filename(__name__,
                                                  'xtb/default_settings/necessary_files/fragments/CC_H8C3_d91b46644317dee9c2b868166c66a18c~1.charges'),
                'fragments_coord' : resource_filename(__name__,
                                                  'xtb/default_settings/necessary_files/fragments/CC_H8C3_d91b46644317dee9c2b868166c66a18c~1.xtbscan.log'),
                'fragments_angle' : resource_filename(__name__,
                                                  'xtb/default_settings/necessary_files/fragments/CC_H8C3_d91b46644317dee9c2b868166c66a18c~1.dat'),
                'torsiondrive_charge': resource_filename(__name__,
                                                  'xtb/torsiondrive/necessary_files/CC_H8C3_d91b46644317dee9c2b868166c66a18c~1.charges'),
                'torsiondrive_energy': resource_filename(__name__,
                                                  'xtb/torsiondrive/necessary_files/CC_H8C3_d91b46644317dee9c2b868166c66a18c~1.log')
                }
                
xTB_DMF = {'xyz_file': resource_filename(__name__,
                                                  'xtb/DMF/DMF.xyz'),
                'wbo_file': resource_filename(__name__,
                                                  'xtb/DMF/necessary_files/DMF_hessian.wbo'),
                'hess_file': resource_filename(__name__,
                                                  'xtb/DMF/necessary_files/DMF_hessian.hessian'),
                'pc_file': resource_filename(__name__,
                                                  'xtb/DMF/necessary_files/DMF_hessian.charges'),
                'coord_file': resource_filename(__name__,
                                                  'xtb/DMF/necessary_files/DMF_hessian.xtbopt.xyz'),
                }
