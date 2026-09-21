import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGES_DIR = os.path.join(SCRIPT_DIR, "images")
os.makedirs(IMAGES_DIR, exist_ok=True)

# -------------------------------------------------------------
# DIAGRAM 1: LAYERED ARCHITECTURE OVERVIEW
# -------------------------------------------------------------
def create_diagram_1(output_path):
    fig, ax = plt.subplots(figsize=(14, 10), dpi=300)
    fig.patch.set_facecolor('#F8FAFC')
    ax.set_facecolor('#F8FAFC')
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(7, 9.5, "Layered Architecture Pattern (N-Tier)", fontsize=22, fontweight='bold', ha='center', color='#0F172A', fontfamily='sans-serif')
    ax.text(7, 9.15, "Component Breakdown & Interaction in /home/anil/Desktop/Layered", fontsize=12, ha='center', color='#475569', fontfamily='sans-serif')

    # Layers data: (name, file, role, color, border, y_pos)
    layers = [
        ("1. Presentation / Application Entry Layer", "main.py", "User interface entry point, input ingestion, and service orchestration", "#3B82F6", "#1D4ED8", 7.4),
        ("2. Service / Business Logic Layer (BLL)", "service/employee_service.py", "Business rules, validation, calculations, orchestrating DAO calls", "#10B981", "#047857", 5.4),
        ("3. Data Access Object Layer (DAO / DAL)", "dao/employee_dao.py", "Database operations, SQL query construction, persistence logic", "#F59E0B", "#B45309", 3.4),
        ("4. Infrastructure / Database Layer", "database/connection.py & MySQL Server", "Connection management, driver handling, and relational storage (pdemployee1)", "#8B5CF6", "#6D28D9", 1.4)
    ]

    for title, filename, desc, bg_col, border_col, y in layers:
        # Layer Card
        rect = patches.FancyBboxPatch((1.0, y - 0.7), 8.8, 1.4, boxstyle="round,pad=0.15,rounding_size=0.2",
                                      facecolor='white', edgecolor=border_col, linewidth=2.0)
        ax.add_patch(rect)
        
        # Color bar on the left
        bar = patches.FancyBboxPatch((1.0, y - 0.7), 0.35, 1.4, boxstyle="round,pad=0.0,rounding_size=0.1",
                                     facecolor=bg_col, edgecolor='none')
        ax.add_patch(bar)

        # Header Pill
        pill = patches.FancyBboxPatch((1.6, y + 0.25), len(filename) * 0.16 + 0.3, 0.32,
                                      boxstyle="round,pad=0.05,rounding_size=0.1",
                                      facecolor='#F1F5F9', edgecolor='#CBD5E1', linewidth=1)
        ax.add_patch(pill)
        ax.text(1.75, y + 0.32, filename, fontsize=10, fontweight='bold', fontfamily='monospace', color='#0F172A', va='center')

        # Title and Description
        ax.text(1.6, y - 0.05, title, fontsize=13, fontweight='bold', color='#1E293B', fontfamily='sans-serif', va='center')
        ax.text(1.6, y - 0.4, desc, fontsize=10.5, color='#64748B', fontfamily='sans-serif', va='center')

    # Flow arrows between layers
    for y in [6.7, 4.7, 2.7]:
        # Request Arrow (Down)
        ax.annotate('', xy=(4.5, y - 0.65), xytext=(4.5, y),
                    arrowprops=dict(facecolor='#0284C7', edgecolor='#0284C7', width=2.5, headwidth=9, headlength=7, shrink=0.05))
        ax.text(4.8, y - 0.3, "Request / Call ↓", fontsize=9, fontweight='bold', color='#0284C7', va='center')

        # Response Arrow (Up)
        ax.annotate('', xy=(6.5, y), xytext=(6.5, y - 0.65),
                    arrowprops=dict(facecolor='#059669', edgecolor='#059669', width=2.5, headwidth=9, headlength=7, shrink=0.05))
        ax.text(6.8, y - 0.3, "Result / Data ↑", fontsize=9, fontweight='bold', color='#059669', va='center')

    # Cross-Cutting Model Card on Right
    model_rect = patches.FancyBboxPatch((10.3, 0.7), 3.0, 8.1, boxstyle="round,pad=0.15,rounding_size=0.25",
                                        facecolor='#FFFBEB', edgecolor='#F59E0B', linewidth=2.2, linestyle='--')
    ax.add_patch(model_rect)

    ax.text(11.8, 8.3, "Cross-Cutting Layer", fontsize=12, fontweight='bold', ha='center', color='#B45309')
    ax.text(11.8, 7.9, "model/employee.py", fontsize=11, fontweight='bold', ha='center', fontfamily='monospace', color='#1E293B')
    
    # Model content box
    m_box = patches.FancyBboxPatch((10.6, 3.8), 2.4, 3.7, boxstyle="round,pad=0.1,rounding_size=0.15",
                                   facecolor='white', edgecolor='#FCD34D', linewidth=1.5)
    ax.add_patch(m_box)

    ax.text(11.8, 7.1, "Class: Employee", fontsize=11, fontweight='bold', ha='center', color='#0F172A')
    ax.plot([10.8, 12.8], [6.85, 6.85], color='#E2E8F0', linewidth=1)
    
    ax.text(10.8, 6.45, "• id: int", fontsize=10, fontfamily='monospace', color='#334155')
    ax.text(10.8, 6.05, "• name: str", fontsize=10, fontfamily='monospace', color='#334155')
    ax.text(10.8, 5.65, "• salary: float", fontsize=10, fontfamily='monospace', color='#334155')
    
    ax.plot([10.8, 12.8], [5.35, 5.35], color='#E2E8F0', linewidth=1)
    ax.text(10.8, 4.95, "__init__(id, name, salary)", fontsize=9, fontfamily='monospace', color='#2563EB')
    ax.text(10.8, 4.25, "Data Transfer Object\n(DTO) transferred\nacross all layers", fontsize=9, fontstyle='italic', color='#64748B', ha='left')

    # DTO flow indicators
    ax.annotate('', xy=(9.8, 7.4), xytext=(10.3, 7.4),
                arrowprops=dict(arrowstyle='<->', color='#D97706', lw=2, linestyle=':'))
    ax.annotate('', xy=(9.8, 5.4), xytext=(10.3, 5.4),
                arrowprops=dict(arrowstyle='<->', color='#D97706', lw=2, linestyle=':'))
    ax.annotate('', xy=(9.8, 3.4), xytext=(10.3, 3.4),
                arrowprops=dict(arrowstyle='<->', color='#D97706', lw=2, linestyle=':'))

    ax.text(11.8, 2.0, "Carries data across\nboundaries without\nexposing internal\ndatabase logic.", 
            fontsize=9.5, ha='center', color='#78350F', fontstyle='italic')

    plt.tight_layout()
    plt.savefig(output_path, dpi=300, facecolor=fig.get_facecolor(), edgecolor='none', bbox_inches='tight')
    plt.close()
    print(f"Diagram 1 saved to {output_path}")


# -------------------------------------------------------------
# DIAGRAM 2: EXECUTION & DATA FLOW SEQUENCE
# -------------------------------------------------------------
def create_diagram_2(output_path):
    fig, ax = plt.subplots(figsize=(15, 11), dpi=300)
    fig.patch.set_facecolor('#F8FAFC')
    ax.set_facecolor('#F8FAFC')
    ax.set_xlim(0, 15)
    ax.set_ylim(0, 11)
    ax.axis('off')

    # Header
    ax.text(7.5, 10.5, "End-to-End Execution Flow (add_employee Workflow)", fontsize=20, fontweight='bold', ha='center', color='#0F172A')
    ax.text(7.5, 10.15, "Trace of s1.add_employee(Employee(10, 'Anil Yadav', 99999)) execution", fontsize=12, ha='center', color='#475569')

    # Lifelines columns (x-positions)
    lifelines = [
        ("Client / UI\n(main.py)", 2.0, "#3B82F6"),
        ("Model Entity\n(Employee)", 4.5, "#EAB308"),
        ("Service Layer\n(EmployeeService)", 7.5, "#10B981"),
        ("DAO Layer\n(EmployeeDao)", 10.5, "#F97316"),
        ("Database / MySQL\n(test.pdemployee1)", 13.5, "#8B5CF6")
    ]

    for name, x, col in lifelines:
        # Header box
        box = patches.FancyBboxPatch((x - 1.1, 8.8), 2.2, 0.9, boxstyle="round,pad=0.1,rounding_size=0.15",
                                     facecolor=col, edgecolor='#1E293B', linewidth=1.5)
        ax.add_patch(box)
        ax.text(x, 9.25, name, fontsize=9.5, fontweight='bold', color='white', ha='center', va='center')
        # Vertical lifeline
        ax.plot([x, x], [0.8, 8.7], color='#94A3B8', linestyle='--', linewidth=1.2, zorder=0)

    # Sequence steps (y_pos, from_x, to_x, label, sublabel, color)
    steps = [
        (8.1, 2.0, 4.5, "1. Instantiate Employee", "Employee(10, 'Anil Yadav', 99999)", "#3B82F6", False),
        (7.2, 4.5, 2.0, "2. Returns Employee instance", "Reference to employee object (emp)", "#64748B", True),
        (6.3, 2.0, 7.5, "3. s1.add_employee(emp)", "Passes Employee DTO to business layer", "#0284C7", False),
        (5.3, 7.5, 10.5, "4. d1.save_employee(emp)", "Delegates database persistence to DAO", "#059669", False),
        (4.3, 10.5, 13.5, "5. Database().connect()", "Establishes MySQL connection (localhost/test)", "#D97706", False),
        (3.4, 10.5, 13.5, "6. cursor.execute(query, data)", "INSERT INTO pdemployee1 VALUES (10, 'Anil Yadav', 99999)", "#7C3AED", False),
        (2.4, 10.5, 13.5, "7. conn.commit()", "Persists transaction changes to storage", "#7C3AED", False),
        (1.5, 13.5, 10.5, "8. Confirmation", "Row inserted successfully in pdemployee1", "#059669", True),
        (0.9, 10.5, 2.0, "9. Status Printout", "'Data saved successfully!!' to console", "#10B981", True)
    ]

    for y, x1, x2, label, sublabel, col, is_return in steps:
        style = '--' if is_return else '-'
        # Arrow
        ax.annotate('', xy=(x2, y), xytext=(x1, y),
                    arrowprops=dict(arrowstyle='->' if is_return else '-|>', color=col, lw=2.2, linestyle=style, shrinkA=3, shrinkB=3))
        
        # Label card above arrow
        mid_x = (x1 + x2) / 2
        ax.text(mid_x, y + 0.28, label, fontsize=9.5, fontweight='bold', color=col, ha='center', va='bottom',
                bbox=dict(boxstyle='round,pad=0.2', facecolor='#FFFFFF', edgecolor='#CBD5E1', lw=0.8))
        if sublabel:
            ax.text(mid_x, y - 0.28, sublabel, fontsize=8, color='#475569', ha='center', va='top', fontfamily='monospace' if '(' in sublabel else 'sans-serif')

    plt.tight_layout()
    plt.savefig(output_path, dpi=300, facecolor=fig.get_facecolor(), edgecolor='none', bbox_inches='tight')
    plt.close()
    print(f"Diagram 2 saved to {output_path}")


# -------------------------------------------------------------
# DIAGRAM 3: COMPONENT RESPONSIBILITY MATRIX
# -------------------------------------------------------------
def create_diagram_3(output_path):
    fig, ax = plt.subplots(figsize=(15, 10), dpi=300)
    fig.patch.set_facecolor('#F8FAFC')
    ax.set_facecolor('#F8FAFC')
    ax.set_xlim(0, 15)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Header
    ax.text(7.5, 9.5, "Component Responsibility & Boundaries", fontsize=21, fontweight='bold', ha='center', color='#0F172A')
    ax.text(7.5, 9.15, "Separation of Concerns (SoC) across the Layered Project Directory", fontsize=11.5, ha='center', color='#475569')

    # Columns: Component / File, Layer Type, Primary Responsibilities, Strict Anti-Patterns (What NOT to do)
    headers = ["Layer / Module", "Primary Responsibilities", "Strict Boundaries (What it NEVER does)"]
    col_x = [0.8, 4.2, 9.8]
    col_w = [3.2, 5.4, 4.4]

    # Header row
    for i, h in enumerate(headers):
        box = patches.FancyBboxPatch((col_x[i], 8.3), col_w[i], 0.6, boxstyle="round,pad=0.05,rounding_size=0.1",
                                     facecolor='#0F172A', edgecolor='none')
        ax.add_patch(box)
        ax.text(col_x[i] + col_w[i]/2, 8.6, h, fontsize=10.5, fontweight='bold', color='white', ha='center', va='center')

    # Rows data
    rows = [
        ("Presentation Layer\nmain.py", "#3B82F6",
         "• Application entry point\n• Consumes user input & prints output\n• Instantiates Model objects\n• Coordinates Service layer calls",
         "• NEVER writes SQL queries\n• NEVER connects to Database directly\n• NEVER executes low-level persistence", 6.8),

        ("Service Layer (BLL)\nservice/employee_service.py", "#10B981",
         "• Implements business rules & workflows\n• Validates input ranges & formats\n• Orchestrates multiple DAO operations\n• Converts raw errors to business results",
         "• NEVER contains raw SQL statements\n• NEVER manages DB connections/pools\n• NEVER parses HTTP/CLI arguments directly", 5.2),

        ("Data Access Layer (DAO)\ndao/employee_dao.py", "#F59E0B",
         "• Translates model objects into SQL\n• Executes CRUD operations (INSERT/SELECT)\n• Handles SQL query parameters (%s tokens)\n• Commits transactions (conn.commit())",
         "• NEVER applies business rules (e.g. salary checks)\n• NEVER interacts with User Interface\n• NEVER hardcodes DB host credentials", 3.6),

        ("Infrastructure / DB\ndatabase/connection.py", "#8B5CF6",
         "• Centralizes MySQL connection parameters\n• Provides reusable connection factory\n• Manages network socket/connection pool",
         "• NEVER knows about Employee or any Entity\n• NEVER executes specific domain SQL\n• NEVER contains business logic", 2.0),

        ("Model Entity (DTO)\nmodel/employee.py", "#0284C7",
         "• Encapsulates employee attributes\n• Provides pure data representation (state)\n• Decouples layers from dicts/tuples",
         "• NEVER contains DB connection or SQL\n• NEVER contains UI rendering logic", 0.6)
    ]

    for title, col, do_txt, dont_txt, y in rows:
        h_box = 1.35 if "Model" in title else 1.45
        
        # Col 1: Title Card
        c1 = patches.FancyBboxPatch((col_x[0], y), col_w[0], h_box, boxstyle="round,pad=0.08,rounding_size=0.1",
                                    facecolor='white', edgecolor=col, linewidth=2)
        ax.add_patch(c1)
        ax.plot([col_x[0], col_x[0] + 0.25], [y + h_box/2, y + h_box/2], color=col, linewidth=6)
        ax.text(col_x[0] + 0.4, y + h_box/2, title, fontsize=10.5, fontweight='bold', color='#1E293B', va='center')

        # Col 2: Do Card
        c2 = patches.FancyBboxPatch((col_x[1], y), col_w[1], h_box, boxstyle="round,pad=0.08,rounding_size=0.1",
                                    facecolor='white', edgecolor='#CBD5E1', linewidth=1)
        ax.add_patch(c2)
        ax.text(col_x[1] + 0.3, y + h_box - 0.25, do_txt, fontsize=9.2, color='#334155', va='top', linespacing=1.4)

        # Col 3: Don't Card
        c3 = patches.FancyBboxPatch((col_x[2], y), col_w[2], h_box, boxstyle="round,pad=0.08,rounding_size=0.1",
                                    facecolor='#FEF2F2', edgecolor='#FCA5A5', linewidth=1)
        ax.add_patch(c3)
        ax.text(col_x[2] + 0.3, y + h_box - 0.25, dont_txt, fontsize=9.2, color='#991B1B', va='top', linespacing=1.4)

    plt.tight_layout()
    plt.savefig(output_path, dpi=300, facecolor=fig.get_facecolor(), edgecolor='none', bbox_inches='tight')
    plt.close()
    print(f"Diagram 3 saved to {output_path}")


# -------------------------------------------------------------
# DIAGRAM 4: UML CLASS & DATABASE SCHEMA DIAGRAM
# -------------------------------------------------------------
def create_diagram_4(output_path):
    fig, ax = plt.subplots(figsize=(15, 10), dpi=300)
    fig.patch.set_facecolor('#F8FAFC')
    ax.set_facecolor('#F8FAFC')
    ax.set_xlim(0, 15)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Header
    ax.text(7.5, 9.6, "UML Class Diagram & Relational Mapping", fontsize=21, fontweight='bold', ha='center', color='#0F172A')
    ax.text(7.5, 9.2, "Class Structures, Inter-Class Dependencies, and MySQL Table Schema", fontsize=12, ha='center', color='#475569')

    # Box 1: Employee Class (Model)
    b_emp = patches.FancyBboxPatch((0.8, 5.2), 3.4, 3.2, boxstyle="round,pad=0.08,rounding_size=0.12",
                                  facecolor='white', edgecolor='#0284C7', linewidth=2)
    ax.add_patch(b_emp)
    ax.text(2.5, 8.0, "«Entity / Model»\nEmployee", fontsize=11, fontweight='bold', ha='center', color='#0369A1')
    ax.plot([0.8, 4.2], [7.5, 7.5], color='#CBD5E1', lw=1.2)
    ax.text(1.1, 7.1, "+ id: int\n+ name: str\n+ salary: float", fontsize=10, fontfamily='monospace', color='#334155', linespacing=1.5)
    ax.plot([0.8, 4.2], [6.1, 6.1], color='#CBD5E1', lw=1.2)
    ax.text(1.1, 5.65, "+ __init__(id, name, salary)", fontsize=9.5, fontfamily='monospace', color='#2563EB')

    # Box 2: EmployeeService Class
    b_srv = patches.FancyBboxPatch((5.4, 5.2), 4.2, 3.2, boxstyle="round,pad=0.08,rounding_size=0.12",
                                  facecolor='white', edgecolor='#10B981', linewidth=2)
    ax.add_patch(b_srv)
    ax.text(7.5, 8.0, "«Service»\nEmployeeService", fontsize=11, fontweight='bold', ha='center', color='#047857')
    ax.plot([5.4, 9.6], [7.5, 7.5], color='#CBD5E1', lw=1.2)
    ax.text(5.7, 7.0, "# Dependencies\n- dao: EmployeeDao", fontsize=10, fontfamily='monospace', color='#64748B')
    ax.plot([5.4, 9.6], [6.3, 6.3], color='#CBD5E1', lw=1.2)
    ax.text(5.7, 5.75, "+ displayemployee(): void\n+ add_employee(emp: Employee)", fontsize=9.5, fontfamily='monospace', color='#065F46', linespacing=1.6)

    # Box 3: EmployeeDao Class
    b_dao = patches.FancyBboxPatch((10.4, 5.2), 4.0, 3.2, boxstyle="round,pad=0.08,rounding_size=0.12",
                                  facecolor='white', edgecolor='#F59E0B', linewidth=2)
    ax.add_patch(b_dao)
    ax.text(12.4, 8.0, "«Data Access Object»\nEmployeeDao", fontsize=11, fontweight='bold', ha='center', color='#B45309')
    ax.plot([10.4, 14.4], [7.5, 7.5], color='#CBD5E1', lw=1.2)
    ax.text(10.7, 7.0, "# Dependencies\n- db: Database", fontsize=10, fontfamily='monospace', color='#64748B')
    ax.plot([10.4, 14.4], [6.3, 6.3], color='#CBD5E1', lw=1.2)
    ax.text(10.7, 5.75, "+ getemployee(): void\n+ save_employee(emp: Employee)", fontsize=9.5, fontfamily='monospace', color='#92400E', linespacing=1.6)

    # Box 4: Database Class
    b_db = patches.FancyBboxPatch((10.4, 1.2), 4.0, 2.6, boxstyle="round,pad=0.08,rounding_size=0.12",
                                 facecolor='white', edgecolor='#8B5CF6', linewidth=2)
    ax.add_patch(b_db)
    ax.text(12.4, 3.4, "«Infrastructure»\nDatabase", fontsize=11, fontweight='bold', ha='center', color='#6D28D9')
    ax.plot([10.4, 14.4], [2.95, 2.95], color='#CBD5E1', lw=1.2)
    ax.text(10.7, 2.6, "- host: str = 'localhost'\n- user: str = 'root'\n- database: str = 'test'", fontsize=9, fontfamily='monospace', color='#475569')
    ax.plot([10.4, 14.4], [1.95, 1.95], color='#CBD5E1', lw=1.2)
    ax.text(10.7, 1.5, "+ connect() -> MySQLConnection", fontsize=9.2, fontfamily='monospace', color='#5B21B6')

    # Box 5: MySQL Table Schema
    b_tbl = patches.FancyBboxPatch((5.4, 1.2), 4.2, 2.6, boxstyle="round,pad=0.08,rounding_size=0.12",
                                  facecolor='#F5F3FF', edgecolor='#A78BFA', linewidth=2, linestyle='--')
    ax.add_patch(b_tbl)
    ax.text(7.5, 3.4, "«RDBMS Table»\nMySQL: test.pdemployee1", fontsize=11, fontweight='bold', ha='center', color='#5B21B6')
    ax.plot([5.4, 9.6], [2.95, 2.95], color='#C4B5FD', lw=1.2)
    ax.text(5.7, 2.55, "PK: id INT\n    name VARCHAR(255)\n    salary DECIMAL(10,2)", fontsize=9.5, fontfamily='monospace', color='#312E81', linespacing=1.4)
    ax.plot([5.4, 9.6], [1.75, 1.75], color='#C4B5FD', lw=1.2)
    ax.text(5.7, 1.45, "Engine: InnoDB (ACID Compliant)", fontsize=8.5, fontstyle='italic', color='#6D28D9')

    # Relationships & Arrows
    # Service -> Dao (uses / instantiates)
    ax.annotate('', xy=(10.4, 6.8), xytext=(9.6, 6.8),
                arrowprops=dict(facecolor='#1E293B', edgecolor='#1E293B', width=1.5, headwidth=8, headlength=7))
    ax.text(10.0, 7.05, "«instantiates»", fontsize=8, ha='center', color='#475569')

    # Dao -> Database (uses)
    ax.annotate('', xy=(12.4, 3.8), xytext=(12.4, 5.2),
                arrowprops=dict(facecolor='#1E293B', edgecolor='#1E293B', width=1.5, headwidth=8, headlength=7))
    ax.text(12.7, 4.5, "«calls connect()»", fontsize=8.5, ha='left', color='#475569')

    # Dao -> Table (persists SQL)
    ax.annotate('', xy=(9.6, 2.5), xytext=(10.4, 2.5),
                arrowprops=dict(facecolor='#8B5CF6', edgecolor='#8B5CF6', width=1.5, headwidth=8, headlength=7))
    ax.text(10.0, 2.75, "«executes SQL»", fontsize=8, ha='center', color='#6D28D9')

    # Model -> Service & DAO (Dependency)
    ax.annotate('', xy=(4.2, 6.8), xytext=(5.4, 6.8),
                arrowprops=dict(arrowstyle='<-', color='#0284C7', lw=2, linestyle=':'))
    ax.text(4.8, 7.05, "«uses»", fontsize=8, ha='center', color='#0284C7')

    plt.tight_layout()
    plt.savefig(output_path, dpi=300, facecolor=fig.get_facecolor(), edgecolor='none', bbox_inches='tight')
    plt.close()
    print(f"Diagram 4 saved to {output_path}")


# -------------------------------------------------------------
# DIAGRAM 5: MONOLITHIC SPAGHETTI VS LAYERED ARCHITECTURE
# -------------------------------------------------------------
def create_diagram_5(output_path):
    fig, ax = plt.subplots(figsize=(15, 9), dpi=300)
    fig.patch.set_facecolor('#F8FAFC')
    ax.set_facecolor('#F8FAFC')
    ax.set_xlim(0, 15)
    ax.set_ylim(0, 9)
    ax.axis('off')

    # Header
    ax.text(7.5, 8.5, "Monolithic Script vs. Layered Architecture", fontsize=21, fontweight='bold', ha='center', color='#0F172A')
    ax.text(7.5, 8.1, "Why professional enterprise applications adopt Layered Architecture", fontsize=12, ha='center', color='#475569')

    # Left: Monolithic Anti-Pattern
    card_bad = patches.FancyBboxPatch((0.8, 0.8), 6.3, 6.8, boxstyle="round,pad=0.15,rounding_size=0.2",
                                      facecolor='#FEF2F2', edgecolor='#EF4444', linewidth=2)
    ax.add_patch(card_bad)

    ax.text(3.95, 7.2, "[POOR DESIGN] Monolithic Script", fontsize=15, fontweight='bold', ha='center', color='#B91C1C')
    ax.text(3.95, 6.8, "(Everything inside one script.py file)", fontsize=10, ha='center', color='#7F1D1D')

    # Bad points code snippet mockup
    code_box = patches.FancyBboxPatch((1.2, 3.4), 5.5, 3.1, boxstyle="round,pad=0.1,rounding_size=0.1",
                                      facecolor='#1E293B', edgecolor='#334155')
    ax.add_patch(code_box)
    code_text = (
        "# script.py (High Coupling, Low Cohesion)\n"
        "import mysql.connector\n"
        "id = int(input('Enter ID: ')) # UI + Input\n"
        "if id <= 0: raise Error()      # Business rule\n"
        "conn = mysql.connect(...)     # DB connect\n"
        "cur.execute('INSERT...')      # SQL Query\n"
        "print('Done!')                 # UI Output"
    )
    ax.text(1.4, 6.2, code_text, fontsize=8.8, fontfamily='monospace', color='#F8FAFC', va='top', linespacing=1.35)

    bad_features = [
        "- Tight Coupling: DB change breaks entire script",
        "- Zero Reusability: Cannot reuse logic in web/API/CLI",
        "- Untestable: Cannot unit test logic without real DB",
        "- Spaghetti Maintenance: High risk of regressions",
        "- High Security Risk: Vulnerable to SQL injections"
    ]
    ax.text(1.2, 3.1, "\n".join(bad_features), fontsize=9.5, color='#991B1B', linespacing=1.45)

    # Right: Layered Architecture Pattern
    card_good = patches.FancyBboxPatch((7.9, 0.8), 6.3, 6.8, boxstyle="round,pad=0.15,rounding_size=0.2",
                                       facecolor='#F0FDF4', edgecolor='#10B981', linewidth=2)
    ax.add_patch(card_good)

    ax.text(11.05, 7.2, "[BEST PRACTICE] Layered Architecture", fontsize=15, fontweight='bold', ha='center', color='#047857')
    ax.text(11.05, 6.8, "(Organized into Model, Service, DAO, and Database)", fontsize=10, ha='center', color='#065F46')

    # Good structure mockup
    good_box = patches.FancyBboxPatch((8.3, 3.4), 5.5, 3.1, boxstyle="round,pad=0.1,rounding_size=0.1",
                                      facecolor='#FFFFFF', edgecolor='#A7F3D0', linewidth=1.5)
    ax.add_patch(good_box)
    good_text = (
        "project_root/\n"
        " |-- main.py                 (Client / Presentation)\n"
        " |-- model/employee.py       (Domain Entity DTO)\n"
        " |-- service/                (Business Logic & Validation)\n"
        " |-- dao/                    (Data Access & SQL)\n"
        " +-- database/               (DB Pool & Connection)"
    )
    ax.text(8.5, 6.2, good_text, fontsize=9.5, fontfamily='monospace', color='#065F46', va='top', linespacing=1.35)

    good_features = [
        "- Separation of Concerns (SoC): Clean responsibilities",
        "- Loose Coupling: Swap MySQL for PostgreSQL easily",
        "- 100% Testable: Mock DAO to unit-test service logic",
        "- Enterprise Scalability: Clean team collaboration",
        "- Security: Centralized parameterized queries"
    ]
    ax.text(8.3, 3.1, "\n".join(good_features), fontsize=9.5, color='#166534', linespacing=1.45)

    plt.tight_layout()
    plt.savefig(output_path, dpi=300, facecolor=fig.get_facecolor(), edgecolor='none', bbox_inches='tight')
    plt.close()
    print(f"Diagram 5 saved to {output_path}")


if __name__ == "__main__":
    create_diagram_1(os.path.join(IMAGES_DIR, "01_layered_architecture_overview.png"))
    create_diagram_2(os.path.join(IMAGES_DIR, "02_execution_data_flow.png"))
    create_diagram_3(os.path.join(IMAGES_DIR, "03_component_responsibility_matrix.png"))
    create_diagram_4(os.path.join(IMAGES_DIR, "04_uml_class_diagram.png"))
    create_diagram_5(os.path.join(IMAGES_DIR, "05_monolithic_vs_layered.png"))
    print("All 5 diagrams successfully generated!")
