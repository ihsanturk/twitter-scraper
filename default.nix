{ pkgs, lib, buildPythonPackage, docopt, selenium }:

buildPythonPackage rec {
	pname = "ihsan-twitter";
	version = "0.0.1";

	src = ./.;
	doCheck = false;
	propagatedBuildInputs = [
		docopt
		selenium
	];

	meta = with lib; {
		description = "Twitter scraping and stream.";
		homepage = "https://github.com/ihsanturk/ihsan-twitter";
		license = licenses.mit;
		# maintainers = [ maintainers.ihsanturk ];
	};

}
