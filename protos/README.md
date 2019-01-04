Run:

```
make createvirtualenv
make buildit-accounts
```

Then change the absolute imports to relative ones:
i.e.

```
from accounts import accounts_pb2 as accounts_dot_accounts__pb2

```

becomes

```
from . import accounts_pb2 as accounts_dot_accounts__pb2
```