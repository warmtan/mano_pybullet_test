export MANO_MODELS_DIR='/home/robot/Desktop/mano_pybullet_test/data/mano_v1_2/models/'
# python -m mano_pybullet.tools.gui_control --dofs 20 --right-hand --no-visual-shapes --no-self-collisions
# python -m mano_pybullet.tools.gui_control --dofs 20 --left-hand
python tests/test_hand_lift_env.py
