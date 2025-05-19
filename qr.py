import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask
from PIL import Image

# Configurazione QR code
qr = qrcode.QRCode(
    version=None,  # Auto-select version
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=15,  # Aumentato per migliore leggibilità
    border=4
)

qr.add_data('https://github.com/Egy98')
qr.make(fit=True)

# Percorsi file
logo_path = r"inserisci\qui\il\tuo\path\GitHub-Mark.png"
output_path = r"inserisci\qui\il\tuo\path\qr_final_github.png"

# Carica e prepara il logo
try:
    logo = Image.open(logo_path)
    base_img = qr.make_image(image_factory=StyledPilImage)
    logo_size = min(base_img.size) // 4
    logo = logo.resize((logo_size, logo_size), Image.LANCZOS)
except Exception as e:
    print(f"Errore caricamento logo: {e}")
    logo = None

# Crea QR code
img = qr.make_image(
    image_factory=StyledPilImage,
    module_drawer=RoundedModuleDrawer(),
    color_mask=RadialGradiantColorMask(
        back_color=(255, 255, 255),
        center_color=(70, 130, 180),
        edge_color=(0, 0, 139)
    ),
    embeded_image=logo if logo else None
)

img.save(output_path)
print(f"QR code salvato in: {output_path}")
