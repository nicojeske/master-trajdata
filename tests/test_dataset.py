import unittest
from collections import defaultdict

import torch
from torch.utils.data import DataLoader
from tqdm import tqdm

from trajdata import AgentBatch, AgentType, UnifiedDataset, SceneBatch
from trajdata.visualization import plot_scene_batch
from trajdata.visualization.interactive_animation import (
    InteractiveAnimation,
    animate_agent_batch_interactive,
)
from trajdata.visualization.interactive_vis import plot_agent_batch_interactive
from trajdata.visualization.vis import plot_agent_batch


class TestDataset(unittest.TestCase):
    # def test_dataloading(self):
    #     dataset = UnifiedDataset(
    #         desired_data=["nusc_mini-mini_val"],
    #         centric="agent",
    #         desired_dt=0.1,
    #         history_sec=(3.2, 3.2),
    #         future_sec=(4.8, 4.8),
    #         only_predict=[AgentType.VEHICLE],
    #         agent_interaction_distances=defaultdict(lambda: 30.0),
    #         incl_robot_future=True,
    #         incl_raster_map=True,
    #         standardize_data=False,
    #         raster_map_params={
    #             "px_per_m": 2,
    #             "map_size_px": 224,
    #             "offset_frac_xy": (-0.5, 0.0),
    #         },
    #         num_workers=4,
    #         verbose=True,
    #         data_dirs={  # Remember to change this to match your filesystem!
    #             "nusc_mini": "~/datasets/nuScenes",
    #         },
    #     )
    #
    #     dataloader = DataLoader(
    #         dataset,
    #         batch_size=4,
    #         shuffle=True,
    #         collate_fn=dataset.get_collate_fn(),
    #         num_workers=0,
    #     )
    #
    #     i = 0
    #     batch: AgentBatch
    #     for batch in dataloader:
    #         i += 1
    #
    #         batch.to("cuda")
    #
    #         self.assertIsInstance(batch.curr_agent_state, dataset.torch_state_type)
    #         self.assertIsInstance(batch.agent_hist, dataset.torch_obs_type)
    #         self.assertIsInstance(batch.agent_fut, dataset.torch_obs_type)
    #         self.assertIsInstance(batch.robot_fut, dataset.torch_obs_type)
    #
    #         if i == 5:
    #             break
    #
    # def test_dict_dataloading(self):
    #     dataset = UnifiedDataset(
    #         desired_data=["nusc_mini-mini_val"],
    #         centric="agent",
    #         desired_dt=0.1,
    #         history_sec=(3.2, 3.2),
    #         future_sec=(4.8, 4.8),
    #         only_predict=[AgentType.VEHICLE],
    #         agent_interaction_distances=defaultdict(lambda: 30.0),
    #         incl_robot_future=True,
    #         incl_raster_map=True,
    #         standardize_data=False,
    #         raster_map_params={
    #             "px_per_m": 2,
    #             "map_size_px": 224,
    #             "offset_frac_xy": (-0.5, 0.0),
    #         },
    #         num_workers=4,
    #         verbose=True,
    #         data_dirs={  # Remember to change this to match your filesystem!
    #             "nusc_mini": "~/datasets/nuScenes",
    #         },
    #     )
    #
    #     dataloader = DataLoader(
    #         dataset,
    #         batch_size=4,
    #         shuffle=True,
    #         collate_fn=dataset.get_collate_fn(return_dict=True),
    #         num_workers=0,
    #     )
    #
    #     i = 0
    #     for batch in dataloader:
    #         i += 1
    #
    #         self.assertIsInstance(batch["curr_agent_state"], dataset.torch_state_type)
    #         self.assertIsInstance(batch["agent_hist"], dataset.torch_obs_type)
    #         self.assertIsInstance(batch["agent_fut"], dataset.torch_obs_type)
    #         self.assertIsInstance(batch["robot_fut"], dataset.torch_obs_type)
    #
    #         if i == 5:
    #             break
    #
    #     dataset = UnifiedDataset(
    #         desired_data=["nusc_mini-mini_val"],
    #         centric="scene",
    #         desired_dt=0.1,
    #         history_sec=(3.2, 3.2),
    #         future_sec=(4.8, 4.8),
    #         only_predict=[AgentType.VEHICLE],
    #         agent_interaction_distances=defaultdict(lambda: 30.0),
    #         incl_robot_future=True,
    #         incl_raster_map=True,
    #         standardize_data=False,
    #         raster_map_params={
    #             "px_per_m": 2,
    #             "map_size_px": 224,
    #             "offset_frac_xy": (-0.5, 0.0),
    #         },
    #         num_workers=4,
    #         verbose=True,
    #         data_dirs={  # Remember to change this to match your filesystem!
    #             "nusc_mini": "~/datasets/nuScenes",
    #         },
    #     )
    #
    #     dataloader = DataLoader(
    #         dataset,
    #         batch_size=4,
    #         shuffle=True,
    #         collate_fn=dataset.get_collate_fn(return_dict=True),
    #         num_workers=0,
    #     )
    #
    #     i = 0
    #     for batch in dataloader:
    #         i += 1
    #
    #         self.assertIsInstance(
    #             batch["centered_agent_state"], dataset.torch_state_type
    #         )
    #         self.assertIsInstance(batch["agent_hist"], dataset.torch_obs_type)
    #         self.assertIsInstance(batch["agent_fut"], dataset.torch_obs_type)
    #         self.assertIsInstance(batch["robot_fut"], dataset.torch_obs_type)
    #
    #         if i == 5:
    #             break
    #
    # def test_default_datatypes_agent(self):
    #     dataset = UnifiedDataset(
    #         desired_data=["nusc_mini-mini_val"],
    #         centric="agent",
    #         desired_dt=0.1,
    #         history_sec=(3.2, 3.2),
    #         future_sec=(4.8, 4.8),
    #         only_predict=[AgentType.VEHICLE],
    #         agent_interaction_distances=defaultdict(lambda: 30.0),
    #         incl_robot_future=True,
    #         incl_raster_map=True,
    #         standardize_data=False,
    #         raster_map_params={
    #             "px_per_m": 2,
    #             "map_size_px": 224,
    #             "offset_frac_xy": (-0.5, 0.0),
    #         },
    #         num_workers=4,
    #         verbose=True,
    #         data_dirs={  # Remember to change this to match your filesystem!
    #             "nusc_mini": "~/datasets/nuScenes",
    #         },
    #     )
    #
    #     elem: AgentBatchElement = dataset[0]
    #     self.assertIsInstance(elem.curr_agent_state_np, dataset.np_state_type)
    #     self.assertIsInstance(elem.agent_history_np, dataset.np_obs_type)
    #     self.assertIsInstance(elem.agent_future_np, dataset.np_obs_type)
    #     self.assertIsInstance(elem.robot_future_np, dataset.np_obs_type)
    #
    # def test_default_datatypes_scene(self):
    #     dataset = UnifiedDataset(
    #         desired_data=["nusc_mini-mini_val"],
    #         centric="scene",
    #         desired_dt=0.1,
    #         history_sec=(3.2, 3.2),
    #         future_sec=(4.8, 4.8),
    #         only_predict=[AgentType.VEHICLE],
    #         agent_interaction_distances=defaultdict(lambda: 30.0),
    #         incl_robot_future=True,
    #         incl_raster_map=True,
    #         standardize_data=False,
    #         raster_map_params={
    #             "px_per_m": 2,
    #             "map_size_px": 224,
    #             "offset_frac_xy": (-0.5, 0.0),
    #         },
    #         num_workers=4,
    #         verbose=True,
    #         data_dirs={  # Remember to change this to match your filesystem!
    #             "nusc_mini": "~/datasets/nuScenes",
    #         },
    #     )
    #
    #     elem: SceneBatchElement = dataset[0]
    #     self.assertIsInstance(elem.centered_agent_state_np, dataset.np_state_type)
    #     self.assertIsInstance(elem.agent_histories[0], dataset.np_obs_type)
    #     self.assertIsInstance(elem.agent_futures[0], dataset.np_obs_type)
    #     self.assertIsInstance(elem.robot_future_np, dataset.np_obs_type)


    def test_waymo(self):
        dataset = UnifiedDataset(
            desired_data=["waymo_custom"],
            data_dirs={  # Remember to change this to match your filesystem!
                "waymo_custom": "K:\\Master\\Waymo",
            },
            verbose=True,
            only_predict=None,
            # state_format="x,y,z,xd,yd,h",
            # obs_format="x,y,z,xd,yd,s,c",
            incl_robot_future=False,
            incl_raster_map=False,
            raster_map_params={
                "px_per_m": 2,
                "map_size_px": 224,
                "offset_frac_xy": (-0.5, 0.0),
                "num_workers": 16,
            },
            # only_types=[AgentType.VEHICLE],
            agent_interaction_distances=defaultdict(lambda: 30.0),
            # max_agent_num=20,
            cache_location=r"K:\Master\.trajdata_cache",
            num_workers=0,
            incl_vector_map=True,
            vector_map_params={
                "incl_road_lanes": True,
                "incl_road_areas": True,
                "incl_ped_crosswalks": True,
                "incl_ped_walkways": True,
                "collate": True,
                "keep_in_memory": False
            },
            centric="agent"  # All agents at one time step,

        )

        dataloader = DataLoader(
            dataset,
            batch_size=1,
            shuffle=False,
            collate_fn=dataset.get_collate_fn(),
            num_workers=0,
        )

        torch.manual_seed(42)

        i = 0

        # batch: SceneBatch
        # for batch in tqdm(dataloader):
        #     print("Scene: ", batch.scene_ids)
        #
        #     plot_scene_batch(batch, batch_idx=0)
        #
        #     i += 1
        #     if i == 4:
        #         break

        for batch in tqdm(dataloader):
            plot_agent_batch_interactive(batch, batch_idx=0, cache_path=dataset.cache_path)
            plot_agent_batch(batch, batch_idx=0)

            animation = InteractiveAnimation(
                animate_agent_batch_interactive,
                batch=batch,
                batch_idx=0,
                cache_path=dataset.cache_path,
            )
            animation.show()
            break

        # i = 0
        # batch: AgentBatch
        # for batch in dataloader:
        #     i += 1
        #
        #     print(batch.agent_name)
        #     #
        #     # self.assertIsInstance(batch.curr_agent_state, dataset.torch_state_type)
        #     # self.assertIsInstance(batch.agent_hist, dataset.torch_obs_type)
        #     # self.assertIsInstance(batch.agent_fut, dataset.torch_obs_type)
        #     # self.assertIsInstance(batch.robot_fut, dataset.torch_obs_type)
        #
        #     if i == 2:
        #         break

if __name__ == "__main__":
    unittest.main()
