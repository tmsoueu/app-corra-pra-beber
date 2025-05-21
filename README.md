# App Corra Pra Beber

## Como rodar o app

### Modo Desktop (recomendado para simular celular)

O modo desktop permite que o app abra uma janela nativa, onde o tamanho da janela pode ser controlado pelo código (ex: 390x800px para simular um celular).

**Com Poetry:**
```sh
poetry run flet app app_corra_pra_beber/main.py
```

**Com Flet puro:**
```sh
flet app app_corra_pra_beber/main.py
```

### Modo Web

No modo web, o app roda no navegador e o tamanho da janela é controlado pelo navegador, não pelo código. O layout responsivo garante boa experiência, mas o redimensionamento automático não é possível.

**Com Poetry:**
```sh
poetry run flet run -w app_corra_pra_beber/main.py
```

**Com Flet puro:**
```sh
flet run -w app_corra_pra_beber/main.py
```

---

- Para melhor experiência mobile, use o modo desktop.
- O layout do app é responsivo e se adapta a diferentes tamanhos de tela.
- A splash screen exibe o logo localizado em `app_corra_pra_beber/assets/logo.png`.
