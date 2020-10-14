with import <nixpkgs> {};

(
	let ihsan-twitter = pkgs.callPackage ./default.nix {

		pkgs = pkgs;
		docopt = pkgs.python38Packages.docopt;
		selenium = pkgs.python38Packages.selenium;
		buildPythonPackage = pkgs.python38Packages.buildPythonPackage;

	};

	in pkgs.python38.buildEnv.override rec {
		extraLibs = [ ihsan-twitter ];
	}

).env
