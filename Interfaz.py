import tkinter as tk
from tkinter import ttk, messagebox
import math
from Fisica import calcular_fuerza_neta

class AplicacionCoulomb:
    def __init__(self, raiz):
        self.raiz = raiz
        self.raiz.title("Calculadora de Fuerza de Coulomb")
        self.raiz.configure(bg="#0f1117")
        self.raiz.geometry("1100x720")
        self.raiz.minsize(900, 600)

        self.cargas_fuente = []
        self._construir_interfaz()

    def _construir_interfaz(self):
        # Colores del tema oscuro
        self.COLOR_BG       = "#0f1117"
        self.COLOR_PANEL    = "#1a1d27"
        self.COLOR_ACENTO   = "#4f8ef7"
        self.COLOR_TEXTO    = "#e8eaf0"
        self.COLOR_SUBTEXTO = "#8b90a0"
        self.COLOR_BORDE    = "#2a2d3e"
        self.COLOR_POSITIVA = "#4f8ef7"
        self.COLOR_NEGATIVA = "#f76c6c"
        self.COLOR_OBJETIVO = "#f0c040"
        self.COLOR_FNETA    = "#50d890"
        self.FUENTE_TITULO  = ("Consolas", 13, "bold")
        self.FUENTE_NORMAL  = ("Consolas", 11)
        self.FUENTE_CHICA   = ("Consolas", 10)

        frame_izq = tk.Frame(self.raiz, bg=self.COLOR_BG, width=320)
        frame_izq.pack(side=tk.LEFT, fill=tk.Y, padx=(16, 0), pady=16)
        frame_izq.pack_propagate(False)

        frame_der = tk.Frame(self.raiz, bg=self.COLOR_BG)
        frame_der.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=16, pady=16)

        self._crear_panel_entrada(frame_izq)
        self._crear_panel_lista(frame_izq)
        self._crear_panel_resultados(frame_izq)
        self._crear_canvas(frame_der)

    def _crear_panel_entrada(self, padre):
        panel = tk.Frame(padre, bg=self.COLOR_PANEL, highlightbackground=self.COLOR_BORDE, highlightthickness=1)
        panel.pack(fill=tk.X, pady=(0, 10))

        tk.Label(panel, text="── CARGAS FUENTE ──", bg=self.COLOR_PANEL, fg=self.COLOR_ACENTO, font=self.FUENTE_TITULO).pack(pady=(10, 6))

        campos = [("Carga q (μC):", "entrada_q"), ("Posición X (m):", "entrada_x"), ("Posición Y (m):", "entrada_y")]
        for etiqueta, nombre in campos:
            fila = tk.Frame(panel, bg=self.COLOR_PANEL)
            fila.pack(fill=tk.X, padx=12, pady=2)
            tk.Label(fila, text=etiqueta, bg=self.COLOR_PANEL, fg=self.COLOR_SUBTEXTO, font=self.FUENTE_CHICA, width=16, anchor="w").pack(side=tk.LEFT)
            entrada = tk.Entry(fila, bg="#252836", fg=self.COLOR_TEXTO, insertbackground=self.COLOR_TEXTO, relief=tk.FLAT, font=self.FUENTE_NORMAL, width=10)
            entrada.pack(side=tk.LEFT, padx=(4, 0))
            setattr(self, nombre, entrada)

        tk.Button(panel, text="+ Agregar carga", command=self._agregar_carga, bg=self.COLOR_ACENTO, fg="white", relief=tk.FLAT, font=self.FUENTE_NORMAL, cursor="hand2").pack(fill=tk.X, padx=12, pady=(8, 6))

        tk.Label(panel, text="── CARGA OBJETIVO ──", bg=self.COLOR_PANEL, fg=self.COLOR_OBJETIVO, font=self.FUENTE_TITULO).pack(pady=(10, 6))

        campos_obj = [("Carga Q (μC):", "entrada_qobj"), ("Posición X (m):", "entrada_xobj"), ("Posición Y (m):", "entrada_yobj")]
        for etiqueta, nombre in campos_obj:
            fila = tk.Frame(panel, bg=self.COLOR_PANEL)
            fila.pack(fill=tk.X, padx=12, pady=2)
            tk.Label(fila, text=etiqueta, bg=self.COLOR_PANEL, fg=self.COLOR_SUBTEXTO, font=self.FUENTE_CHICA, width=16, anchor="w").pack(side=tk.LEFT)
            entrada = tk.Entry(fila, bg="#252836", fg=self.COLOR_TEXTO, insertbackground=self.COLOR_TEXTO, relief=tk.FLAT, font=self.FUENTE_NORMAL, width=10)
            entrada.pack(side=tk.LEFT, padx=(4, 0))
            setattr(self, nombre, entrada)

        tk.Button(panel, text="Calcular fuerza neta", command=self._calcular, bg="#2ecc71", fg="#0f1117", relief=tk.FLAT, font=("Consolas", 12, "bold"), cursor="hand2").pack(fill=tk.X, padx=12, pady=(10, 12))

    def _crear_panel_lista(self, padre):
        panel = tk.Frame(padre, bg=self.COLOR_PANEL, highlightbackground=self.COLOR_BORDE, highlightthickness=1)
        panel.pack(fill=tk.X, pady=(0, 10))
        cabecera = tk.Frame(panel, bg=self.COLOR_PANEL)
        cabecera.pack(fill=tk.X, padx=12, pady=(10, 4))
        tk.Label(cabecera, text="Cargas ingresadas", bg=self.COLOR_PANEL, fg=self.COLOR_ACENTO, font=self.FUENTE_TITULO).pack(side=tk.LEFT)
        tk.Button(cabecera, text="Limpiar", command=self._limpiar, bg=self.COLOR_BORDE, fg=self.COLOR_SUBTEXTO, relief=tk.FLAT, font=self.FUENTE_CHICA, cursor="hand2").pack(side=tk.RIGHT)
        frame_lista = tk.Frame(panel, bg=self.COLOR_PANEL)
        frame_lista.pack(fill=tk.X, padx=12, pady=(0, 10))
        self.lista_cargas = tk.Listbox(frame_lista, bg="#252836", fg=self.COLOR_TEXTO, selectbackground=self.COLOR_ACENTO, relief=tk.FLAT, font=self.FUENTE_CHICA, height=6, activestyle="none")
        scroll = tk.Scrollbar(frame_lista, orient=tk.VERTICAL, command=self.lista_cargas.yview)
        self.lista_cargas.config(yscrollcommand=scroll.set)
        self.lista_cargas.pack(side=tk.LEFT, fill=tk.X, expand=True)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)

    def _crear_panel_resultados(self, padre):
        panel = tk.Frame(padre, bg=self.COLOR_PANEL, highlightbackground=self.COLOR_BORDE, highlightthickness=1)
        panel.pack(fill=tk.BOTH, expand=True)
        tk.Label(panel, text="── RESULTADOS ──", bg=self.COLOR_PANEL, fg=self.COLOR_FNETA, font=self.FUENTE_TITULO).pack(pady=(10, 6))
        self.texto_resultados = tk.Text(panel, bg="#252836", fg=self.COLOR_TEXTO, relief=tk.FLAT, font=self.FUENTE_CHICA, wrap=tk.WORD, state=tk.DISABLED, padx=8, pady=8)
        self.texto_resultados.pack(fill=tk.BOTH, expand=True, padx=12, pady=(0, 12))
        self.texto_resultados.tag_config("titulo", foreground=self.COLOR_ACENTO, font=("Consolas", 11, "bold"))
        self.texto_resultados.tag_config("resultado", foreground=self.COLOR_FNETA, font=("Consolas", 11, "bold"))
        self.texto_resultados.tag_config("detalle", foreground=self.COLOR_SUBTEXTO)
        self.texto_resultados.tag_config("error", foreground=self.COLOR_NEGATIVA)

    def _crear_canvas(self, padre):
        tk.Label(padre, text="Visualización de cargas y fuerzas", bg=self.COLOR_BG, fg=self.COLOR_SUBTEXTO, font=self.FUENTE_CHICA).pack(anchor="w", pady=(0, 4))
        self.canvas = tk.Canvas(padre, bg="#12151f", relief=tk.FLAT, highlightthickness=1, highlightbackground=self.COLOR_BORDE)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.canvas.bind("<Configure>", lambda e: self._redibujar())
        leyenda = tk.Frame(padre, bg=self.COLOR_BG)
        leyenda.pack(anchor="w", pady=(6, 0))
        items = [(self.COLOR_POSITIVA, "carga + (fuente)"), (self.COLOR_NEGATIVA, "carga − (fuente)"), (self.COLOR_OBJETIVO, "carga objetivo Q"), (self.COLOR_FNETA, "fuerza neta"), ("#aaaaff", "fuerza individual")]
        for color, texto in items:
            tk.Label(leyenda, text="●", fg=color, bg=self.COLOR_BG, font=("Consolas", 13)).pack(side=tk.LEFT)
            tk.Label(leyenda, text=texto + "  ", fg=self.COLOR_SUBTEXTO, bg=self.COLOR_BG, font=self.FUENTE_CHICA).pack(side=tk.LEFT)

    def _agregar_carga(self):
        try:
            q = float(self.entrada_q.get()) * 1e-6
            x = float(self.entrada_x.get())
            y = float(self.entrada_y.get())
        except ValueError:
            messagebox.showerror("Error de entrada", "Por favor ingresa números válidos en todos los campos.")
            return
        self.cargas_fuente.append((q, x, y))
        signo = "+" if q > 0 else ""
        self.lista_cargas.insert(tk.END, f"  q={signo}{q*1e6:.2f} μC  pos=({x},{y})")
        for campo in [self.entrada_q, self.entrada_x, self.entrada_y]:
            campo.delete(0, tk.END)
        self._redibujar()

    def _calcular(self):
        if not self.cargas_fuente:
            messagebox.showwarning("Sin cargas", "Agrega al menos una carga fuente.")
            return
        try:
            q_obj = float(self.entrada_qobj.get()) * 1e-6
            x_obj = float(self.entrada_xobj.get())
            y_obj = float(self.entrada_yobj.get())
        except ValueError:
            messagebox.showerror("Error", "Ingresa valores válidos para la carga objetivo.")
            return

        self.q_objetivo = (q_obj, x_obj, y_obj)
        qs = [c[0] for c in self.cargas_fuente]
        poss = [(c[1], c[2]) for c in self.cargas_fuente]

        try:
            # Llamada a la función del módulo fisica.py
            Fx, Fy, magnitud, individuales = calcular_fuerza_neta(qs, poss, q_obj, (x_obj, y_obj))
        except ValueError as e:
            self._escribir_resultado(f"Error: {e}", tag="error")
            return

        self._escribir_resultado("", limpiar=True)
        self._escribir_resultado("Fuerzas individuales:\n", tag="titulo")
        for i, (fx, fy) in enumerate(individuales):
            mag_i = math.sqrt(fx**2 + fy**2)
            self._escribir_resultado(f"  F{i+1} = <{fx:.3e}, {fy:.3e}> N\n  |F{i+1}| = {mag_i:.3e} N\n", tag="detalle")
        self._escribir_resultado("─" * 28 + "\n", tag="detalle")
        self._escribir_resultado("Fuerza neta:\n", tag="titulo")
        self._escribir_resultado(f"  F_neta = <{Fx:.4e}, {Fy:.4e}> N\n  |F_neta| = {magnitud:.4e} N\n", tag="resultado")
        angulo = math.degrees(math.atan2(Fy, Fx))
        self._escribir_resultado(f"  Ángulo = {angulo:.2f}°\n", tag="detalle")

        self.fuerzas_individuales = individuales
        self.F_neta = (Fx, Fy)
        self._redibujar()

    def _limpiar(self):
        self.cargas_fuente.clear()
        self.lista_cargas.delete(0, tk.END)
        self._escribir_resultado("", limpiar=True)
        if hasattr(self, "q_objetivo"): del self.q_objetivo
        if hasattr(self, "F_neta"): del self.F_neta
        self._redibujar()

    def _escribir_resultado(self, texto, tag="normal", limpiar=False):
        self.texto_resultados.config(state=tk.NORMAL)
        if limpiar: self.texto_resultados.delete("1.0", tk.END)
        self.texto_resultados.insert(tk.END, texto, tag)
        self.texto_resultados.config(state=tk.DISABLED)

    def _redibujar(self):
        self.canvas.delete("all")
        W, H = self.canvas.winfo_width(), self.canvas.winfo_height()
        if W < 2 or H < 2: return

        todos_x = [c[1] for c in self.cargas_fuente]
        todos_y = [c[2] for c in self.cargas_fuente]
        if hasattr(self, "q_objetivo"):
            todos_x.append(self.q_objetivo[1])
            todos_y.append(self.q_objetivo[2])

        if not todos_x:
            self._dibujar_grid(W, H, 0, 0, 60)
            return

        cx, cy = sum(todos_x)/len(todos_x), sum(todos_y)/len(todos_y)
        rango = max(max(todos_x)-min(todos_x), max(todos_y)-min(todos_y), 1)
        escala = min(W, H) * 0.55 / rango

        def mundo_a_canvas(x, y):
            return W/2 + (x-cx)*escala, H/2 - (y-cy)*escala

        self._dibujar_grid(W, H, cx, cy, escala)

        if hasattr(self, "q_objetivo") and hasattr(self, "fuerzas_individuales"):
            ox, oy = mundo_a_canvas(self.q_objetivo[1], self.q_objetivo[2])
            for Fx, Fy in self.fuerzas_individuales:
                mag = math.sqrt(Fx**2 + Fy**2)
                if mag == 0: continue
                esc_f = min(W, H) * 0.15 / mag
                self._dibujar_flecha(ox, oy, ox + Fx*esc_f, oy - Fy*esc_f, "#6666cc", ancho=1.5)

        if hasattr(self, "q_objetivo") and hasattr(self, "F_neta"):
            ox, oy = mundo_a_canvas(self.q_objetivo[1], self.q_objetivo[2])
            Fx, Fy = self.F_neta
            mag = math.sqrt(Fx**2 + Fy**2)
            if mag > 0:
                esc_f = min(W, H) * 0.20 / mag
                self._dibujar_flecha(ox, oy, ox + Fx*esc_f, oy - Fy*esc_f, self.COLOR_FNETA, ancho=3)

        RADIO = 18
        for q, x, y in self.cargas_fuente:
            px, py = mundo_a_canvas(x, y)
            color = self.COLOR_POSITIVA if q >= 0 else self.COLOR_NEGATIVA
            self.canvas.create_oval(px-RADIO, py-RADIO, px+RADIO, py+RADIO, fill=color, outline="white")
            self.canvas.create_text(px, py, text="+" if q>=0 else "−", fill="white", font=("Consolas", 14, "bold"))
            self.canvas.create_text(px, py+RADIO+10, text=f"{q*1e6:.1f}μC\n({x},{y})", fill=color, font=("Consolas", 9), justify=tk.CENTER)

        if hasattr(self, "q_objetivo"):
            q, x, y = self.q_objetivo
            px, py = mundo_a_canvas(x, y)
            self.canvas.create_oval(px-20, py-20, px+20, py+20, fill=self.COLOR_OBJETIVO, outline="white", width=2)
            self.canvas.create_text(px, py, text="Q", fill="#0f1117", font=("Consolas", 13, "bold"))
            self.canvas.create_text(px, py+30, text=f"{q*1e6:.1f}μC\n({x},{y})", fill=self.COLOR_OBJETIVO, font=("Consolas", 9), justify=tk.CENTER)

    def _dibujar_grid(self, W, H, cx, cy, escala):
        paso_mundo = 1.0
        while escala * paso_mundo < 40: paso_mundo *= 2
        paso_px = escala * paso_mundo
        origen_px, origen_py = W/2, H/2
        x0 = origen_px % paso_px
        while x0 < W:
            self.canvas.create_line(x0, 0, x0, H, fill="#1e2235")
            x0 += paso_px
        y0 = origen_py % paso_px
        while y0 < H:
            self.canvas.create_line(0, y0, W, y0, fill="#1e2235")
            y0 += paso_px
        self.canvas.create_line(0, H/2, W, H/2, fill="#2a2d3e")
        self.canvas.create_line(W/2, 0, W/2, H, fill="#2a2d3e")

    def _dibujar_flecha(self, x1, y1, x2, y2, color, ancho=2):
        self.canvas.create_line(x1, y1, x2, y2, fill=color, width=ancho)
        angulo = math.atan2(y2 - y1, x2 - x1)
        tam_punta = 12
        p1x, p1y = x2 - tam_punta * math.cos(angulo - 0.4), y2 - tam_punta * math.sin(angulo - 0.4)
        p2x, p2y = x2 - tam_punta * math.cos(angulo + 0.4), y2 - tam_punta * math.sin(angulo + 0.4)
        self.canvas.create_polygon(x2, y2, p1x, p1y, p2x, p2y, fill=color, outline=color)