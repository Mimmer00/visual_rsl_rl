from .actor_critic import ActorCritic
from .visual_actor_critic import VisualActorCritic

ACTOR_CRITIC_REGISTRY = {
    "mlp": ActorCritic,
    "visual": VisualActorCritic,
}
