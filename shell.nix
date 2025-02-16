{ pkgs ? import <nixpkgs> {}}:

pkgs.mkShell{
  buildInputs = with pkgs; [
    python3
    uv
    python3Packages.opencv4
    python3Packages.google-generativeai
    python3Packages.pytesseract
    python3Packages.python-dotenv
    python3Packages.absl-py
    pkgs.tesseract
  ];
  shellHook = ''
    echo "[✅] Nix Environment Ready"
  '';
}
