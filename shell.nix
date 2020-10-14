with import <nixpkgs> {}; {
	devEnv = stdenv.mkDerivation {
		name = "dev";
		buildInputs = [
			go
			stdenv
			glibc.static
		];

		CFLAGS="-I${pkgs.glibc.dev}/include";
		LDFLAGS="-L${pkgs.glibc}/lib";

		shellHook = ''
			export GOPATH=$HOME/go
		'';

	};
}
