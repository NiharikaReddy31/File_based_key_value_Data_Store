##### File based Key-Value datastore

Supports basic CRUD (Create, Read,Update, Delete) Operations.

**Functionalities:**

1. It can be initialized using an optional file path. If one is not provided, it will reliably create one reasonable location on laptop.
2. Key string capped at 32 characters and Value must be a JSON object capped at 16KB.
3. Every key supports setting a Time-To-Live property when it is created. This property is optional. If provided, it will be evaluated as an integer defining the number of seconds. Once the Time-To-Live for a key has expired, the key will no longer be available for Read or Delete operations.
4. Only one process can access the datastore (local file) at a time.
5. Thread safe.

**Usage:**

###### Create

```
import main as m
m.create("Niharika",1)
m.create("Nikitha",2,150)
```

###### Read

```
m.read("Niharika")
```

###### Update

```
m.update("Niharika",10)
```

###### Delete

```
m.delete("Niharika")
```