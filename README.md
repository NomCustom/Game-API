# Game-API
La seule et unique API REST de jeux française !

### Mais comment utiliser l'API ?

C'est simple ! Vous aurez plusieurs exemples ici:

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

url = "

'''
Expected outputs: 
{

}
'''
