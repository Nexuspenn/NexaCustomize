#!/bin/bash
APPID="org.nexuspenn.nexaos.customize"
BUNDLENAME="nexacustomize.flatpak"
flatpak-builder --install --user --force-clean flatpak-app "$APPID".yml

if [ "$1" = "bundle" ]; then
	flatpak build-bundle ~/.local/share/flatpak/repo "$BUNDLENAME" "$APPID"
fi
