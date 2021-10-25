# ARGUMENTS to runme.sh
# angle_start : smallest anglemof attack (degrees)
# angle_stop  : biggest angle of attack (degrees)
# n_angles    : split angle_stop-angle_start into n_angles parts
# n_nodes     : number of nodes on one side of airfoil
# n_levels    : number of refinement steps in meshing 0=no refinement 1=one time 2=two times etc...
chmod +x runme.sh
./runme.sh 0 30 10 200 1
echo "*./runme complete "
cd msh
dolfin-convert r0a0n200.msh r0a0n200.xml
cd ..
cd ..
cd navier_stokes_solver
echo "*Starting ./airfoil  "
./airfoil  10 0.1 10. 1 ../cloudnaca/msh/r0a0n200.xml
