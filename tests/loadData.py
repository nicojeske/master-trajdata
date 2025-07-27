import enum
from pathlib import Path
from collections import defaultdict

import matplotlib.pyplot as plt
import torch
from torch.utils.data import DataLoader
from trajdata import UnifiedDataset, SceneBatch, AgentType, MapAPI
from trajdata.data_structures import Scene, SceneBatchElement, StateArray
from trajdata.maps.vec_map_elements import RoadLane
from trajdata.visualization import plot_scene_batch

def __main__():

    cache_path = Path(r"K:\Master\.trajdata_cache")
    map_api = MapAPI(cache_path)

    dataset = UnifiedDataset(
        desired_data=["waymo_custom"],
        data_dirs={  # Remember to change this to match your filesystem!
            "waymo_custom": "K:\\Master\\Waymo",
        },
        verbose=True,
        only_predict=None,
        state_format="x,y,z,xd,yd,h",
        obs_format="x,y,z,xd,yd,s,c",
        standardize_data=False,
        incl_robot_future=False,
        incl_raster_map=True,
        raster_map_params={
            "px_per_m": 2,
            "map_size_px": 224,
            "offset_frac_xy": (-0.5, 0.0),
            "num_workers": 0,
        },
        # only_types=[AgentType.VEHICLE],
        agent_interaction_distances=defaultdict(lambda: 30.0),
        # max_agent_num=20,
        cache_location=cache_path,
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
        centric="scene" # All agents at one time step,

    )

    # Create a DataLoader to load the actual scene data
    # The dataset is already configured for scene-centric loading.
    dataloader = DataLoader(
        dataset,
        batch_size=1,  # Load one scene at a time
        shuffle=False, # Keep the order consistent, load scene 0 first
        collate_fn=dataset.get_collate_fn(), # Use the dataset's collate function
        num_workers=0 # Use 0 workers for simplicity, adjust as needed
    )

    # Get the first batch (which contains the first scene's data)
    # We use next(iter(...)) to get the first element without a loop.
    first_batch: SceneBatch = next(iter(dataloader))

    # Now 'first_batch' contains the fully loaded data for the first scene(s)
    # including agent trajectories and map information as configured.
    # You can inspect its contents, e.g.:
    print(f"Loaded batch for scene(s): {first_batch.scene_ids}")
    print(f"Number of agents in first scene: {first_batch.num_agents[0]}")
    print(f"Agent history shape: {first_batch.agent_hist.shape}")
    if first_batch.vector_maps:
        print(f"Vector map included for scene: {first_batch.vector_maps[0].map_id}")
    if first_batch.maps is not None:
        print(f"Raster map shape: {first_batch.maps.shape}")
