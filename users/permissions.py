from rest_framework.permissions import BasePermission
from videos.models import Video


class PlanPermission(BasePermission):

    def has_permission(self, request, view):
        movie_id = view.kwargs["pk"]
        movie = Video.objects.get(id=movie_id)
        user = request.user

        match movie.required_plan:
            case "bronze":
                res = (
                    True
                    if user.plan.plane_name == "bronze"
                    or user.plan.plane_name == "silver"
                    or user.plan.plane_name == "gold"
                    else False
                )
                return res
            case "silver":
                res = (
                    True
                    if user.plan.plane_name == "silver"
                    or user.plan.plane_name == "gold"
                    else False
                )
                return res
            case "gold":
                res = True if user.plan.plane_name == "gold" else False
                return res
