import tkinter as tk
from tkinter import ttk, messagebox

# --- 1. SCORING DATABASE (The Brain) ---
CPU_DB = {
    "Snapdragon": {
        "8 Gen 3": 100, "8 Gen 2": 90, "8+ Gen 1": 85, "8 Gen 1": 80, 
        "7+ Gen 2": 75, "778G": 55, "695": 40, "680": 30
    },
    "MediaTek": {
        "Dimensity 9300": 98, "Dimensity 9200": 88, "Dimensity 8300": 78,
        "Dimensity 7200": 65, "Dimensity 6020": 40, "Helio G99": 35
    },
    "Apple": {
        "A17 Pro": 105, "A16 Bionic": 95, "A15 Bionic": 88, "A14 Bionic": 78
    },
    "Google": {
        "Tensor G3": 82, "Tensor G2": 75, "Tensor G1": 65
    }
}

SCREEN_SCORES = {
    "LTPO AMOLED (120Hz+)": 35,
    "Super AMOLED (120Hz)": 30,
    "OLED (90Hz+)": 25,
    "IPS LCD (120Hz)": 15,
    "IPS LCD (60Hz)": 10,
    "TFT LCD": 5
}

STORAGE_SCORES = {
    "128 GB": 10, "256 GB": 20, "512 GB": 35, "1 TB": 50
}

# --- 2. THEMING ---
COLORS = {
    "bg": "#2b2b2b",       
    "panel": "#383838",    
    "accent": "#00adb5",   
    "text": "#eeeeee",     
    "danger": "#ff2e63",   
    "success": "#00e676",
    "warning": "#ffcc00",
    "terminal_bg": "#121212",
    "terminal_fg": "#00ff00"
}

def setup_theme():
    style = ttk.Style()
    style.theme_use("clam")

    style.configure("TFrame", background=COLORS["bg"])
    style.configure("TLabel", background=COLORS["bg"], foreground=COLORS["text"], font=("Segoe UI", 10))
    style.configure("Panel.TLabel", background=COLORS["panel"], foreground=COLORS["text"], font=("Segoe UI", 9))
    style.configure("Header.TLabel", background=COLORS["bg"], foreground=COLORS["accent"], font=("Segoe UI", 16, "bold"))
    
    style.configure("TLabelframe", background=COLORS["panel"], relief="flat", borderwidth=10)
    style.configure("TLabelframe.Label", background=COLORS["panel"], foreground=COLORS["accent"], font=("Segoe UI", 10, "bold"))

    style.configure("TButton", font=("Segoe UI", 10, "bold"), padding=6)
    style.map("TButton", background=[("active", COLORS["accent"])], foreground=[("active", "white")])
    
    style.configure("Action.TButton", background=COLORS["accent"], foreground="white")
    style.configure("Add.TButton", background=COLORS["panel"], foreground=COLORS["text"], borderwidth=1)
    
    style.configure("Green.Horizontal.TProgressbar", troughcolor=COLORS["panel"], background=COLORS["success"], bordercolor=COLORS["panel"], lightcolor=COLORS["success"], darkcolor=COLORS["success"])

# --- 3. UI COMPONENTS ---

class ProductPanel:
    def __init__(self, parent_frame, index):
        self.frame = ttk.LabelFrame(parent_frame, text=f" Device {index+1} ", padding=15)
        self.frame.pack(side="left", padx=10, fill="y")

        # Row 1
        ttk.Label(self.frame, text="Model Name:", style="Panel.TLabel").grid(row=0, column=0, sticky="w", pady=2)
        self.entry_name = tk.Entry(self.frame, width=20, bg="#222", fg="white", insertbackground="white", relief="flat")
        self.entry_name.grid(row=1, column=0, sticky="ew", pady=(0,10))

        ttk.Label(self.frame, text="Price (₹):", foreground=COLORS["danger"], style="Panel.TLabel").grid(row=2, column=0, sticky="w", pady=2)
        self.entry_price = tk.Entry(self.frame, width=20, bg="#222", fg="white", insertbackground="white", relief="flat")
        self.entry_price.grid(row=3, column=0, sticky="ew", pady=(0,10))

        # Row 2
        ttk.Label(self.frame, text="RAM (GB):", style="Panel.TLabel").grid(row=4, column=0, sticky="w")
        self.ram_slider = tk.Scale(self.frame, from_=4, to=24, orient="horizontal", 
                                   bg=COLORS["panel"], fg=COLORS["text"], highlightthickness=0, resolution=2)
        self.ram_slider.set(8)
        self.ram_slider.grid(row=5, column=0, sticky="ew")

        ttk.Label(self.frame, text="Storage:", style="Panel.TLabel").grid(row=6, column=0, sticky="w", pady=(10,0))
        self.storage_cb = ttk.Combobox(self.frame, values=list(STORAGE_SCORES.keys()), state="readonly")
        self.storage_cb.current(1) 
        self.storage_cb.grid(row=7, column=0, sticky="ew")

        # Row 3
        ttk.Label(self.frame, text="Screen Type:", foreground=COLORS["accent"], style="Panel.TLabel").grid(row=8, column=0, sticky="w", pady=(10,0))
        self.screen_type_cb = ttk.Combobox(self.frame, values=list(SCREEN_SCORES.keys()), state="readonly")
        self.screen_type_cb.current(3) 
        self.screen_type_cb.grid(row=9, column=0, sticky="ew")

        # Row 4
        ttk.Label(self.frame, text="Battery (mAh):", style="Panel.TLabel").grid(row=10, column=0, sticky="w", pady=(10,0))
        self.battery_slider = tk.Scale(self.frame, from_=3000, to=6500, orient="horizontal", 
                                       bg=COLORS["panel"], fg=COLORS["text"], highlightthickness=0, resolution=100)
        self.battery_slider.set(5000)
        self.battery_slider.grid(row=11, column=0, sticky="ew")

        ttk.Label(self.frame, text="Charging (Watts):", style="Panel.TLabel").grid(row=12, column=0, sticky="w", pady=(5,0))
        self.charge_slider = tk.Scale(self.frame, from_=15, to=120, orient="horizontal", 
                                       bg=COLORS["panel"], fg=COLORS["text"], highlightthickness=0, resolution=5)
        self.charge_slider.set(33)
        self.charge_slider.grid(row=13, column=0, sticky="ew")

        # Row 5
        ttk.Label(self.frame, text="Processor Brand:", style="Panel.TLabel").grid(row=14, column=0, sticky="w", pady=(10,0))
        self.brand_cb = ttk.Combobox(self.frame, values=list(CPU_DB.keys()), state="readonly")
        self.brand_cb.set("Snapdragon")
        self.brand_cb.grid(row=15, column=0, sticky="ew")
        
        self.model_cb = ttk.Combobox(self.frame, state="readonly")
        self.model_cb.grid(row=16, column=0, sticky="ew", pady=2)

        self.brand_cb.bind("<<ComboboxSelected>>", self.update_models)
        self.update_models(None)

    def update_models(self, event):
        brand = self.brand_cb.get()
        models = list(CPU_DB.get(brand, {}).keys())
        self.model_cb['values'] = models
        if models: self.model_cb.current(0)

    def get_data(self):
        name = self.entry_name.get() or "Unknown Device"
        try:
            price = float(self.entry_price.get())
        except ValueError:
            price = 1.0

        ram = self.ram_slider.get()
        storage_txt = self.storage_cb.get()
        battery = self.battery_slider.get()
        charging = self.charge_slider.get()
        screen_type = self.screen_type_cb.get()
        brand = self.brand_cb.get()
        model = self.model_cb.get()
        
        # Scoring Logic
        cpu_points = CPU_DB.get(brand, {}).get(model, 0)
        screen_points = SCREEN_SCORES.get(screen_type, 10)
        storage_points = STORAGE_SCORES.get(storage_txt, 0)
        battery_points = (battery / 500) 
        charging_points = (charging / 10)

        raw_score = (cpu_points * 1.5) + (screen_points * 1.2) + (ram * 3) + storage_points + battery_points + charging_points
        vfm_score = (raw_score / price) * 1000 if price > 0 else 0

        return {
            "name": name,
            "price": price,
            "raw_score": raw_score,
            "vfm_score": vfm_score,
            "tech": f"{brand} {model}"
        }

class ResultWindow:
    def __init__(self, master, data_points, user_budget):
        self.top = tk.Toplevel(master)
        self.top.title("Analysis Results")
        self.top.geometry("750x650") # Slightly taller for more text
        self.top.configure(bg=COLORS["terminal_bg"])
        self.data = data_points
        self.budget = user_budget
        
        x = master.winfo_x() + 50
        y = master.winfo_y() + 50
        self.top.geometry(f"+{x}+{y}")

        self.frame = tk.Frame(self.top, bg=COLORS["terminal_bg"])
        self.frame.pack(fill="both", expand=True, padx=20, pady=20)

        self.start_loading_animation()

    def start_loading_animation(self):
        self.lbl_status = tk.Label(self.frame, text="CALCULATING BASELINE...", 
                                   font=("Consolas", 14, "bold"), 
                                   bg=COLORS["terminal_bg"], fg=COLORS["accent"])
        self.lbl_status.pack(pady=(100, 20))

        self.progress = ttk.Progressbar(self.frame, orient="horizontal", length=400, mode="determinate", style="Green.Horizontal.TProgressbar")
        self.progress.pack()
        self.progress_val = 0
        self.animate_loading()

    def animate_loading(self):
        if self.progress_val < 100:
            self.progress_val += 5
            self.progress['value'] = self.progress_val
            if self.progress_val == 40: self.lbl_status.config(text="CHECKING MARKET VALUE...")
            if self.progress_val == 80: self.lbl_status.config(text="FINDING SMART SAVINGS...")
            self.top.after(40, self.animate_loading)
        else:
            self.lbl_status.destroy()
            self.progress.destroy()
            self.show_results()

    def show_results(self):
        self.res_text = tk.Text(self.frame, font=("Consolas", 11), 
                                bg=COLORS["terminal_bg"], fg=COLORS["terminal_fg"], 
                                relief="flat", padx=10, pady=10)
        self.res_text.pack(fill="both", expand=True)

        # 1. Calculate Baseline (Average Score)
        total_score = sum(d['raw_score'] for d in self.data)
        avg_score = total_score / len(self.data)
        
        report = []
        report.append(" MARKET ANALYSIS ".center(65, "="))
        report.append(f"MARKET BASELINE SCORE: {int(avg_score)} pts")
        
        if self.budget > 0:
            report.append(f"YOUR BUDGET: ₹{int(self.budget)}")
        else:
            report.append("YOUR BUDGET: UNLIMITED")
            
        report.append("-" * 65)
        report.append(f"{'DEVICE':<18} | {'PRICE':<9} | {'SCORE':<5} | {'STATUS'}")
        report.append("-" * 65)

        sorted_data = sorted(self.data, key=lambda x: x['raw_score'], reverse=True)

        for item in sorted_data:
            status = "BELOW AVG"
            if item['raw_score'] >= avg_score: status = "SUPERB"
            elif item['raw_score'] >= avg_score * 0.90: status = "GOOD"
            elif item['raw_score'] >= avg_score * 0.80: status = "MID"
            
            line = f"{item['name'][:18]:<18} | ₹{int(item['price']):<8} | {int(item['raw_score']):<5} | {status}"
            report.append(line)
        
        report.append("=" * 65)
        
        # --- THE INTELLIGENT VERDICT LOGIC ---
        report.append("\n💡 ADVISOR VERDICT:")

        if self.budget > 0:
            in_budget = [d for d in self.data if d['price'] <= self.budget]
            over_budget = [d for d in self.data if d['price'] > self.budget]
            
            # --- SCENARIO 1: NOTHING IN BUDGET ---
            if not in_budget:
                cheapest_option = min(self.data, key=lambda x: x['price'])
                diff = cheapest_option['price'] - self.budget
                
                report.append(f"   You cannot afford any of these phones right now.")
                
                if cheapest_option['raw_score'] < avg_score:
                    report.append(f"   ⚠️ WARNING: [{cheapest_option['name']}] is expensive but has MID specs.")
                    report.append(f"   Recommendation: WAIT. Do not buy slightly out of budget trash.")
                else:
                    report.append(f"   ✅ GOOD NEWS: [{cheapest_option['name']}] is excellent.")
                    report.append(f"   Recommendation: WAIT and SAVE the extra ₹{int(diff)}.")
            
            # --- SCENARIO 2: WE HAVE OPTIONS (The Smart Logic) ---
            else:
                # Find the best raw performance within budget
                best_perf_budget = max(in_budget, key=lambda x: x['raw_score'])
                
                # Find the cheapest option within budget that is still "Respectable" (close to baseline)
                # Respectable = Score is at least 90% of the baseline
                respectable_options = [d for d in in_budget if d['raw_score'] >= (avg_score * 0.9)]
                
                if respectable_options:
                    best_value_budget = min(respectable_options, key=lambda x: x['price'])
                else:
                    # If nothing is respectable, just take the best perf one
                    best_value_budget = best_perf_budget

                # CHECK: Do we Save or Spend?
                if best_perf_budget == best_value_budget:
                    # The best performing phone is also the cheapest 'good' phone, or only one option exists.
                    # Now check if we should stretch for an over-budget phone.
                    if over_budget:
                         best_expensive = max(over_budget, key=lambda x: x['raw_score'])
                         perf_gain = (best_expensive['raw_score'] - best_perf_budget['raw_score']) / best_perf_budget['raw_score']
                         cost_gain = (best_expensive['price'] - best_perf_budget['price']) / best_perf_budget['price']
                         
                         if perf_gain > (cost_gain * 0.8):
                             report.append(f"   🛑 HOLD ON. [{best_perf_budget['name']}] fits your budget.")
                             report.append(f"   BUT [{best_expensive['name']}] is a MONSTER update.")
                             report.append(f"   Strategy: Wait to collect ₹{int(best_expensive['price'] - self.budget)} more.")
                         else:
                             report.append(f"   ✅ BUY NOW: [{best_perf_budget['name']}].")
                             report.append(f"   It fits your budget and offers the best performance.")
                    else:
                        report.append(f"   ✅ BUY NOW: [{best_perf_budget['name']}].")
                        report.append(f"   It is the best option you can afford.")

                else:
                    # We have a 'Best Perf' (expensive) and a 'Good Enough' (cheaper) in budget.
                    # Calculate difference
                    price_saved = best_perf_budget['price'] - best_value_budget['price']
                    perf_lost_pct = (best_perf_budget['raw_score'] - best_value_budget['raw_score']) / best_perf_budget['raw_score']
                    
                    # LOGIC: If we save a lot of money (> 15% of budget) for little performance loss (< 10%)
                    if perf_lost_pct < 0.12: # Less than 12% performance drop
                        report.append(f"   💰 SMART SAVER ALERT!")
                        report.append(f"   You CAN afford the [{best_perf_budget['name']}] (₹{int(best_perf_budget['price'])}).")
                        report.append(f"   BUT you should buy the [{best_value_budget['name']}].")
                        report.append(f"   WHY? You save ₹{int(price_saved)} and only lose {int(perf_lost_pct*100)}% speed.")
                        report.append(f"   The [{best_value_budget['name']}] is around market baseline.")
                        report.append(f"   Don't waste money on specs you won't notice.")
                    else:
                        report.append(f"   ✅ BUY THE BEST: [{best_perf_budget['name']}].")
                        report.append(f"   The cheaper [{best_value_budget['name']}] saves money, but is too slow.")
                        report.append(f"   The extra performance is worth the price tag.")

        else:
            # No Budget - Just suggest the highest score
            best_overall = max(self.data, key=lambda x: x['raw_score'])
            report.append(f"   Since you have no budget limit, buy the [{best_overall['name']}].")
            report.append(f"   It is the current baseline leader.")

        self.typewriter_effect(report, 0)

    def typewriter_effect(self, lines, index):
        if index < len(lines):
            self.res_text.insert(tk.END, lines[index] + "\n")
            self.res_text.see(tk.END)
            self.top.after(60, self.typewriter_effect, lines, index + 1)
        else:
            btn_close = ttk.Button(self.top, text="CLOSE WINDOW", command=self.top.destroy, style="Action.TButton")
            btn_close.pack(pady=10)

class CompareApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Phone comarison app 2.0")
        self.root.geometry("1100x750")
        self.root.configure(bg=COLORS["bg"])
        setup_theme()

        header = ttk.Label(root, text="COMPARE A PHONE", style="Header.TLabel")
        header.pack(pady=(20, 5))
        
        sub = ttk.Label(root, text="Smart Analysis: Performance vs Price vs Market Value.", background=COLORS["bg"], foreground="#888")
        sub.pack(pady=(0, 15))

        self.canvas_frame = tk.Frame(root, bg=COLORS["bg"])
        self.canvas_frame.pack(fill="both", expand=True, padx=20)
        
        self.canvas = tk.Canvas(self.canvas_frame, bg=COLORS["bg"], highlightthickness=0) 
        self.scrollbar = ttk.Scrollbar(self.canvas_frame, orient="horizontal", command=self.canvas.xview)
        self.scrollable_frame = tk.Frame(self.canvas, bg=COLORS["bg"])

        self.scrollable_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(xscrollcommand=self.scrollbar.set)
        self.canvas.pack(side="top", fill="both", expand=True)
        self.scrollbar.pack(side="bottom", fill="x", pady=5)

        self.products = []
        self.add_product_column()
        self.add_product_column()

        control_frame = tk.Frame(root, bg=COLORS["bg"])
        control_frame.pack(pady=20)

        btn_add = ttk.Button(control_frame, text="+ ADD DEVICE", command=self.add_product_column, style="Add.TButton")
        btn_add.pack(side="left", padx=10)

        lbl_budget = ttk.Label(control_frame, text="My Budget ₹:", font=("Segoe UI", 11, "bold"))
        lbl_budget.pack(side="left", padx=(30, 5))
        
        self.entry_budget = tk.Entry(control_frame, width=10, bg="#444", fg="white", font=("Segoe UI", 11), insertbackground="white", relief="flat")
        self.entry_budget.pack(side="left", padx=(0, 30), ipady=3)

        btn_run = ttk.Button(control_frame, text="⚡ ADVISE ME", command=self.run_analysis, style="Action.TButton")
        btn_run.pack(side="left", padx=10)

    def add_product_column(self):
        idx = len(self.products)
        new_panel = ProductPanel(self.scrollable_frame, idx)
        self.products.append(new_panel)

    def run_analysis(self):
        data_points = []
        for p in self.products:
            data_points.append(p.get_data())

        if not data_points: return
        
        try:
            budget = float(self.entry_budget.get())
        except ValueError:
            budget = 0.0 

        ResultWindow(self.root, data_points, budget)

if __name__ == "__main__":
    root = tk.Tk()
    app = CompareApp(root)
    root.mainloop()