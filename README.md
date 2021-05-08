# Game-API
La seule et unique API REST de jeux française !

### Mais comment utiliser l'API ?

C'est simple ! Vous aurez plusieurs exemples ici:
Tu veux le lien ? [Clique ici !](https://game-api.jgame.repl.co)

**Obtenir tout les jeux disponibles dans l'API**

```js

GET /api/games/all

```

**Obtenir un jeu par son identifiant**

```js

GET /api/games/(id)

```

**Obtenir le nom d'un jeu par son identifiant**

```js

GET /api/games/(id)/name

```

**Obtenir le créateur d'un jeu par son identifiant**

```js

GET /api/games/(id)/creators

```

**Obtenir le type d'un jeu par son identifiant**

```js

GET /api/games/(id)/type

```

**Obtenir la longue description d'un jeu par son identifiant**

```js

GET /api/games/(id)/long_desc

```

**Obtenir la petite description d'un jeu par son identifiant**

```js

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
```
