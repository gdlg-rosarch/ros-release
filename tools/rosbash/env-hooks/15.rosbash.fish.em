# generated from rosbash/env-hooks/15.rosbash.fish.em

@[if DEVELSPACE]@
. "@(CMAKE_CURRENT_SOURCE_DIR)/rosfish"
@[else]@
if [ -z "$CATKIN_ENV_HOOK_WORKSPACE" ]; then
  CATKIN_ENV_HOOK_WORKSPACE="@(CMAKE_INSTALL_PREFIX)"
fi
. "$CATKIN_ENV_HOOK_WORKSPACE/share/rosbash/rosfish"
@[end if]@
