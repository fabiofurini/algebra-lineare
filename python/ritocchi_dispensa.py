"""Ritocchi di impaginazione della dispensa (non toccano le note).

Ogni voce: (file del capitolo, lingua "it"/"en"/"*", testo nel capitolo
generato, testo che lo sostituisce, motivo). Servono soprattutto a
spezzare su più righe le equazioni che escono dal margine.
"""

RITOCCHI = [
    # --- cap03_vettori ---------------------------------------------------
    ("cap03_vettori", "*",
     r"\(\lambda_1\boldsymbol e_1+\dots+\lambda_n\boldsymbol e_n=\begin{pmatrix}\lambda_1 & \lambda_2 & \dots & \lambda_n\end{pmatrix}'\).",
     r"\[\lambda_1\boldsymbol e_1+\dots+\lambda_n\boldsymbol e_n=\begin{pmatrix}\lambda_1 & \lambda_2 & \dots & \lambda_n\end{pmatrix}'.\]",
     "formula in linea con vettore trasposto: troppo larga, va in display"),

    # --- cap04_matrici ---------------------------------------------------
    ("cap04_matrici", "it",
     "\\end{pmatrix}\n\\qquad \n\\text{oppure, per brevità,}\n\\qquad\n",
     "\\end{pmatrix}\n\\]\noppure, per brevità,\n\\[\n",
     "le due scritture della matrice generica affiancate escono dal margine"),
    ("cap04_matrici", "*",
     "\\end{pmatrix},\n\\qquad\n\\boldsymbol B\\boldsymbol A=",
     "\\end{pmatrix},\n\\]\n\\[\n\\boldsymbol B\\boldsymbol A=",
     "AB e BA affiancati: uno per riga"),
    ("cap04_matrici", "*",
     "\\quad\n\\boldsymbol M_3=\\begin{pmatrix}1 & 0 & 0\\\\ 5 & 2 & 0",
     "\\]\n\\[\n\\boldsymbol M_3=\\begin{pmatrix}1 & 0 & 0\\\\ 5 & 2 & 0",
     "quattro matrici M_1..M_4 su una riga: due per riga"),
    ("cap04_matrici", "it",
     r"\( \Delta_1=q_{11},\ \Delta_2,\ \dots,\ \Delta_n=\det(\boldsymbol Q) \)",
     r"\( \Delta_1=q_{11} \), \( \Delta_2 \), \( \dots \), \( \Delta_n=\det(\boldsymbol Q) \)",
     "elenco in linea non spezzabile"),
    ("cap04_matrici", "it",
     r"\( q_{11},q_{22},q_{33} \)",
     r"\( q_{11} \), \( q_{22} \), \( q_{33} \)",
     "elenco in linea non spezzabile"),
    ("cap04_matrici", "it",
     "\\qquad\\text{cioè}\\qquad\n(-1)^k",
     "\\]\ncioè\n\\[\n(-1)^k",
     "condizione di Sylvester troppo lunga: su due righe"),
    ("cap04_matrici", "en",
     "\\qquad\\text{i.e.}\\qquad\n(-1)^k",
     "\\]\ni.e.\n\\[\n(-1)^k",
     "condizione di Sylvester troppo lunga: su due righe"),

    # --- cap05_norme -----------------------------------------------------
    ("cap05_norme", "*",
     "\\[\n\\left\\| \\begin{pmatrix} 1 \\\\ 0 \\end{pmatrix} \\right\\|_2 = \\sqrt{1^2 + 0^2} = 1, ~\n"
     "\\left\\| \\begin{pmatrix} 0 \\\\ 1 \\end{pmatrix} \\right\\|_2 = \\sqrt{0^2 + 1^2} = 1, ~\n"
     "\\left\\| \\begin{pmatrix} -1 \\\\ 0 \\end{pmatrix} \\right\\|_2 = \\sqrt{(-1)^2 + 0^2} = 1, ~\n"
     "\\left\\| \\begin{pmatrix} 0 \\\\ -1 \\end{pmatrix} \\right\\|_2 = \\sqrt{0^2 + (-1)^2} = 1\n\\]",
     "\\[\n\\begin{aligned}\n"
     "\\left\\| \\begin{pmatrix} 1 \\\\ 0 \\end{pmatrix} \\right\\|_2 &= \\sqrt{1^2 + 0^2} = 1, &\n"
     "\\left\\| \\begin{pmatrix} 0 \\\\ 1 \\end{pmatrix} \\right\\|_2 &= \\sqrt{0^2 + 1^2} = 1,\\\\[1ex]\n"
     "\\left\\| \\begin{pmatrix} -1 \\\\ 0 \\end{pmatrix} \\right\\|_2 &= \\sqrt{(-1)^2 + 0^2} = 1, &\n"
     "\\left\\| \\begin{pmatrix} 0 \\\\ -1 \\end{pmatrix} \\right\\|_2 &= \\sqrt{0^2 + (-1)^2} = 1\n"
     "\\end{aligned}\n\\]",
     "quattro norme l2 su una riga: due per riga"),
    ("cap05_norme", "*",
     "\\[\n\\{{{{\\boldsymbol x}}} \\in \\mathbb{R}^2 : \\|{{{{\\boldsymbol x}}}}\\|_{\\boldsymbol{Q}} \\le 1\\}\n=\n\\left\\{\n"
     "\\begin{pmatrix}\nx_1 \\\\[0.3ex]\nx_2\n\\end{pmatrix}\n\\in \\mathbb{R}^2 :\n\\sqrt{4 x_1^2 + x_2^2} \\le 1\n\\right\\}\n=\n",
     "\\[\n\\begin{aligned}\n\\{{{{\\boldsymbol x}}} \\in \\mathbb{R}^2 : \\|{{{{\\boldsymbol x}}}}\\|_{\\boldsymbol{Q}} \\le 1\\}\n&=\n\\left\\{\n"
     "\\begin{pmatrix}\nx_1 \\\\[0.3ex]\nx_2\n\\end{pmatrix}\n\\in \\mathbb{R}^2 :\n\\sqrt{4 x_1^2 + x_2^2} \\le 1\n\\right\\}\n\\\\[1ex]\n&=\n",
     "definizione dell'insieme troppo lunga: su due righe (inizio)"),
    ("cap05_norme", "*",
     "\\frac{x_1^2}{(1/2)^2} + \\frac{x_2^2}{1^2} \\le 1\n\\right\\}\n\\]",
     "\\frac{x_1^2}{(1/2)^2} + \\frac{x_2^2}{1^2} \\le 1\n\\right\\}\n\\end{aligned}\n\\]",
     "definizione dell'insieme troppo lunga: su due righe (fine)"),
    ("cap05_norme", "*",
     "\\[\n\\{{{{\\boldsymbol x}}} \\in \\mathbb{R}^2 : \\|{{{{\\boldsymbol x}}}}\\|_{\\boldsymbol{Q}} \\le 1\\}\n=\n\\left\\{\n"
     "\\begin{pmatrix}\nx_1 \\\\[0.3ex]\nx_2\n\\end{pmatrix}\n\\in \\mathbb{R}^2 :\n\\sqrt{2x_1^2 - 2x_1x_2 + 2x_2^2} \\le 1\n\\right\\}\n=\n",
     "\\[\n\\begin{aligned}\n\\{{{{\\boldsymbol x}}} \\in \\mathbb{R}^2 : \\|{{{{\\boldsymbol x}}}}\\|_{\\boldsymbol{Q}} \\le 1\\}\n&=\n\\left\\{\n"
     "\\begin{pmatrix}\nx_1 \\\\[0.3ex]\nx_2\n\\end{pmatrix}\n\\in \\mathbb{R}^2 :\n\\sqrt{2x_1^2 - 2x_1x_2 + 2x_2^2} \\le 1\n\\right\\}\n\\\\[1ex]\n&=\n",
     "definizione dell'insieme troppo lunga: su due righe (inizio)"),
    ("cap05_norme", "*",
     "2x_1^2 - 2x_1x_2 + 2x_2^2 \\le 1\n\\right\\}\n\\]",
     "2x_1^2 - 2x_1x_2 + 2x_2^2 \\le 1\n\\right\\}\n\\end{aligned}\n\\]",
     "definizione dell'insieme troppo lunga: su due righe (fine)"),
    ("cap05_norme", "*",
     r"\} + \max\{|w_j| : j \in \{1,2,\ldots,n\}\} ~ \text{",
     "\\} \\\\\n&\\qquad + \\max\\{|w_j| : j \\in \\{1,2,\\ldots,n\\}\\} ~ \\text{",
     "passaggio della disuguaglianza triangolare troppo lungo: su due righe"),

    # --- capA_approfondimenti --------------------------------------------
    ("capA_approfondimenti", "*",
     r"$$ {\rm a)}~ n=47,~m=5, \qquad {\rm b)}~ n=-47,~m=5, \qquad {\rm c)}~ n=47,~m=-5, \qquad {\rm d)}~ n=-47,~m=-5$$",
     r"\[\begin{gathered} {\rm a)}~ n=47,~m=5, \qquad {\rm b)}~ n=-47,~m=5, \\ {\rm c)}~ n=47,~m=-5, \qquad {\rm d)}~ n=-47,~m=-5 \end{gathered}\]",
     "quattro casi su una riga: due per riga"),
]
