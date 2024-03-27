from .authors import urlpatterns as authorsurls
from .books import urlpatterns as booksurls
from .dashboard import urlpatterns as dashboardurls
from .orders import urlpatterns as ordersurls
from .publishers import urlpatterns as publisherurls
from .users import urlpatterns as userurls

urlpatterns = userurls + publisherurls + authorsurls + \
    booksurls + ordersurls + dashboardurls
