{
  description = "7600055 - Programação Orientada a Objetos";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
    systems.url = "github:nix-systems/default-linux";
  };

  outputs = {nixpkgs, systems, ...}: let
    inherit (nixpkgs.lib) genAttrs;
    forEachSystem = f: genAttrs (import systems) (system: f nixpkgs.legacyPackages.${system});
  in {
    # nix develop -c zsh
    devShells = forEachSystem (pkgs: {
      default = pkgs.mkShell {
        packages = [
          pkgs.git
          (pkgs.python314.withPackages (ps: with ps; [
            numpy
          ]))
        ];
      };
    });
  };
}