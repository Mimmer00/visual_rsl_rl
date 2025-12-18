from .registry import ACTOR_CRITIC_REGISTRY

def resolve_actor_critic_class(cfg: dict):
    ac_cfg = cfg.get("actor_critic", {})
    ac_type = ac_cfg.get("type", "mlp")
    if ac_type not in ACTOR_CRITIC_REGISTRY:
        raise KeyError(f"Unknown actor_critic.type={ac_type}")
    return ACTOR_CRITIC_REGISTRY[ac_type]
