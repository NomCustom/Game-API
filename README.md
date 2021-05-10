# Game-API
La seule et unique API REST d'infos jeux française !

### Mais comment utiliser l'API ?

C'est simple ! Vous aurez plusieurs exemples ici:
Tu veux le lien ? [Clique ici !](https://game-api.jgame.repl.co)

**Obtenir tout les jeux disponibles dans l'API**

```bash

GET /api/games/all

```

**Obtenir un jeu par son identifiant**

```bash

GET /api/games/(id)

```

**Obtenir le nom d'un jeu par son identifiant**

```bash

GET /api/games/(id)/name

```

**Obtenir le créateur d'un jeu par son identifiant**

```bash

GET /api/games/(id)/creators

```

**Obtenir le type d'un jeu par son identifiant**

```bash

GET /api/games/(id)/type

```

**Obtenir la longue description d'un jeu par son identifiant**

```bash

GET /api/games/(id)/long_desc

```

**Obtenir la petite description d'un jeu par son identifiant**

```bash

GET /api/games/(id)/short_desc

```

# Exemples:
**Python**
```python
import requests

r = requests.get("https://game-api.jgame.repl.co/api/games/1")
print(r)
data = r.json()
print(data['name'])

#Expected outputs: 
#{
# 'id':1,
# 'creators': 'creators',
# 'type': 'type', 
# 'name': 'name',
# 'short_desc': 'short description',
# 'long_desc': 'long description'
#}

# Asynchronous method:
import aiohttp
import asyncio

async def game_api():
   async with aiohttp.ClientSession() as session:
           url = "https://game-api.jgame.repl.co/api/games/1"
           async with session.get(url) as resp:
                       data = await resp.json()
                       print(data['name'])

asyncio.run(game_api())
```

**Golang**
```go
package main

import (
   "io/ioutil"
   "log"
   "net/http"
)

func main() {
   resp, err := http.Get("https://game-api.jgame.repl.co/api/games/1")
   if err != nil {
      log.Fatalln(err)
   }
   body, err := ioutil.ReadAll(resp.Body) 
   if err != nil {
      log.Fatalln(err)
   }
   sb := string(body)
   log.Printf(sb)
}
/* Expected outputs:
{
 'id':1,
 'creators': 'creators',
 'type': 'type',
 'name': 'name',
 'short_desc': 'short description',
 'long_desc': 'long description'
}
*/
```
