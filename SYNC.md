# Sincronización con el repositorio recreado

El repositorio en GitHub fue recreado con la misma URL. El repo local que ya tenés clonado tiene una historia diferente, por lo que hay que re-sincronizar.

## Pasos

### 1. Abrir una terminal en la carpeta del repositorio

```bash
cd ifts24-lab-pln-2026
```

### 2. Guardar cambios locales (si tenés notebooks modificados)

```bash
git stash
```

### 3. Traer la nueva historia del remoto

```bash
git fetch origin
```

### 4. Reemplazar la historia local con la del remoto

```bash
git reset --hard origin/main
```

### 5. Recuperar tus cambios locales

```bash
git stash pop
```

Si aparecen conflictos, resolvelos y después:

```bash
git add .
git commit -m "Cambios locales"
```

### 6. Verificar

```bash
git status
```

Debería decir: `Your branch is up to date with 'origin/main'`.

---

Una vez sincronizado, este archivo se puede borrar.
