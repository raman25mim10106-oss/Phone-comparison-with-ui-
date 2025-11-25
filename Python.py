import tkinter as tk
from tkinter import ttk, messagebox

# --- 1. SCORING DATABASE (The Brain) ---
# CPU Scores (0-100)
CPU_DB = {
    "Snapdragon": {
        "8 Gen 3": 98, "8 Gen 2": 90, "8 Gen 1": 80, "888": 70, "778G": 50, "695": 35
    },
    "MediaTek": {
        "Dimensity 9300": 97, "Dimensity 9200": 88, "Dimensity 7200": 60, "Dimensity 6020": 35
    },
    "Apple": {
        "A17 Pro": 100, "A16 Bionic": 92, "A15 Bionic": 85, "A14 Bionic": 75
    },
    "Google": {
        "Tensor G3": 82, "Tensor G2": 75, "Tensor G1": 65
    }
}

# Screen Type Scores (Added Bonus Points)
SCREEN_SCORES = {
    "LTPO AMOLED": 30,  # Best tech
    "Super AMOLED": 25, # Excellent
    "OLED": 22,         # Very Good
    "IPS LCD": 10,      # Standard
    "TFT LCD": 5        # Basic
}

class ProductPanel:
    """Class representing a single column (Product)"""
    def __init__(self, parent_frame, index):
        self.frame = tk.LabelFrame(parent_frame, text=f" Device {index+1} ", font=("Arial", 11, "bold"), padx=10, pady=10)
        self.frame.pack(side="left", padx=10, fill="y")

        # NAME
        tk.Label(self.frame, text="Model Name:", font=("Arial", 8)).pack(anchor="w")
        self.entry_name = tk.Entry(self.frame, width=22, bg="#0b1b36", fg="white", insertbackground="white")
        self.entry_name.pack(pady=(0, 10))

        # PRICE
        tk.Label(self.frame, text="Price (₹):", font=("Arial", 8, "bold"), fg="#d32f2f").pack(anchor="w")
        self.entry_price = tk.Entry(self.frame, width=22)
        self.entry_price.pack(pady=(0, 10))

        # RAM
        tk.Label(self.frame, text="RAM (GB):", font=("Arial", 8)).pack(anchor="w")
        self.ram_slider = tk.Scale(self.frame, from_=4, to=24, orient="horizontal", tickinterval=0, resolution=2)
        self.ram_slider.set(8)
        self.ram_slider.pack(fill="x", pady=5)

        # SCREEN SIZE
        tk.Label(self.frame, text="Screen Size (Inch):", font=("Arial", 8)).pack(anchor="w")
        self.screen_slider = tk.Scale(self.frame, from_=5.5, to=7.0, orient="horizontal", resolution=0.1)
        self.screen_slider.set(6.1)
        self.screen_slider.pack(fill="x", pady=5)

        # SCREEN TYPE (NEW!)
        tk.Label(self.frame, text="Screen Type:", font=("Arial", 8, "bold"), fg="#2196F3").pack(anchor="w")
        self.screen_type_cb = ttk.Combobox(self.frame, values=list(SCREEN_SCORES.keys()), state="readonly", width=19)
        self.screen_type_cb.current(3) # Default to IPS LCD
        self.screen_type_cb.pack(pady=(0, 10))

        # PROCESSOR
        tk.Label(self.frame, text="Processor:", font=("Arial", 8)).pack(anchor="w")
        self.brand_cb = ttk.Combobox(self.frame, values=list(CPU_DB.keys()), state="readonly", width=19)
        self.brand_cb.set("Snapdragon")
        self.brand_cb.pack(pady=2)
        
        self.model_cb = ttk.Combobox(self.frame, state="readonly", width=19)
        self.model_cb.pack(pady=2)

        # Bind events
        self.brand_cb.bind("<<ComboboxSelected>>", self.update_models)
        self.update_models(None) # Init

    def update_models(self, event):
        brand = self.brand_cb.get()
        models = list(CPU_DB.get(brand, {}).keys())
        self.model_cb['values'] = models
        if models: self.model_cb.current(0)

    def get_data(self):
        """Returns a dictionary of this product's specs and score"""
        name = self.entry_name.get() or "Unnamed Device"
        
        try:
            price = float(self.entry_price.get())
        except ValueError:
            price = 1.0 # Prevent crash

        ram = self.ram_slider.get()
        screen_size = self.screen_slider.get()
        screen_type = self.screen_type_cb.get()
        
        brand = self.brand_cb.get()
        model = self.model_cb.get()
        
        # --- SCORING LOGIC ---
        cpu_points = CPU_DB.get(brand, {}).get(model, 0)
        screen_type_points = SCREEN_SCORES.get(screen_type, 10)
        
        # Formula: CPU + (RAM * 4) + (Size * 5) + Screen Type Bonus
        raw_score = cpu_points + (ram * 4) + (screen_size * 5) + screen_type_points

        # --- VFM FORMULA ---
        # (Score / Price) * 1000
        vfm_score = (raw_score / price) * 1000 if price > 0 else 0

        return {
            "name": name,
            "price": price,
            "raw_score": raw_score,
            "vfm_score": vfm_score,
            "details": f"{ram}GB | {screen_type}",
            "tech": f"{brand} {model}"
        }

class CompareApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🛒 Compare a Phone ")
        # Increased window height slightly to accommodate the larger text box
        self.root.geometry("1100x850")

        # --- Header ---
        tk.Label(root, text="Always Compare Before You Buy", font=("Helvetica", 18, "bold"), fg="#333").pack(pady=10)

        # --- Scrollable Area Setup ---
        # Slightly reduced the canvas height (450 -> 400) to give more room to Results
        self.canvas_frame = tk.Frame(root)
        self.canvas_frame.pack(fill="x", expand=False, padx=10, pady=5)
        self.canvas = tk.Canvas(self.canvas_frame, height=400) 
        self.scrollbar = tk.Scrollbar(self.canvas_frame, orient="horizontal", command=self.canvas.xview)
        self.scrollable_frame = tk.Frame(self.canvas)

        self.scrollable_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(xscrollcommand=self.scrollbar.set)
        self.canvas.pack(side="top", fill="both", expand=True)
        self.scrollbar.pack(side="bottom", fill="x")

        self.products = []
        self.add_product_column()
        self.add_product_column()

        # --- CONTROLS ---
        control_frame = tk.Frame(root)
        control_frame.pack(pady=10)

        btn_add = tk.Button(control_frame, text="➕ Add Device", command=self.add_product_column, 
                            font=("Arial", 11), bg="#E0E0E0")
        btn_add.pack(side="left", padx=20)

        btn_run = tk.Button(control_frame, text="🔍 ANALYZE & DECIDE", command=self.run_analysis, 
                            font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", padx=20)
        btn_run.pack(side="left", padx=20)

        # --- RESULTS AREA (UPDATED) ---
        # Increased height from 14 to 22
        self.result_text = tk.Text(root, height=22, font=("Courier", 10), bg="#1e1e1e", fg="#00ff00")
        # Added expand=True so it fills any remaining vertical space
        self.result_text.pack(padx=20, pady=10, fill="both", expand=True)

    def add_product_column(self):
        idx = len(self.products)
        new_panel = ProductPanel(self.scrollable_frame, idx)
        self.products.append(new_panel)

    def run_analysis(self):
        data_points = []
        for p in self.products:
            data_points.append(p.get_data())

        if not data_points: return

        best_perf = max(data_points, key=lambda x: x['raw_score'])
        best_vfm = max(data_points, key=lambda x: x['vfm_score'])

        self.result_text.delete(1.0, tk.END)
        
        # Table Header
        header = f"{'DEVICE':<18} | {'₹ PRICE':<9} | {'SCORE':<5} | {'VFM':<6} | {'TECH INFO'}\n"
        self.result_text.insert(tk.END, header)
        self.result_text.insert(tk.END, "-"*75 + "\n")

        # Table Rows
        for item in data_points:
            row = f"{item['name']:<18} | {int(item['price']):<9} | {int(item['raw_score']):<5} | {item['vfm_score']:<6.2f} | {item['details']}\n"
            self.result_text.insert(tk.END, row)

        self.result_text.insert(tk.END, "\n" + "="*75 + "\n")
        
        # VERDICT
        self.result_text.insert(tk.END, f"🚀 PERFORMANCE KING: {best_perf['name']} ({int(best_perf['raw_score'])} pts)\n")
        self.result_text.insert(tk.END, f"   Why? Great mix of CPU ({best_perf['tech']}) and Screen.\n\n")

        self.result_text.insert(tk.END, f"💰 VALUE FOR MONEY: {best_vfm['name']} (Index: {best_vfm['vfm_score']:.2f})\n")
        
        if best_perf == best_vfm:
            self.result_text.insert(tk.END, f"🌟 VERDICT: Buying {best_perf['name']} is a no-brainer. Best specs AND price.")
        else:
            diff = best_perf['price'] - best_vfm['price']
            if diff > 0:
                self.result_text.insert(tk.END, f"💡 VERDICT: The {best_perf['name']} is stronger, but costs ₹{int(diff)} more.\n")
                self.result_text.insert(tk.END, f"   If you are on a budget, buy the {best_vfm['name']}.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CompareApp(root)
    root.mainloop()