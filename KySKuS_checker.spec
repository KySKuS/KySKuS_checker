Name:           KySKuS_checker
Version:        1.0
Release:        1%{?dist}
Summary:        Advanced file integrity monitor with CLI and diff logging
License:        MIT
Requires:       coreutils, diffutils
BuildArch:      noarch
%description
Мониторинг системных файлов
Настройки-
-задержка
-список файлов
-автостарт
%files
%attr(0755,root,root) /usr/local/bin/check.sh
%attr(0755,root,root) /usr/local/bin/kyskus-checker
%attr(0644,root,root) /usr/lib/systemd/system/check.service
%config(noreplace) /etc/KySKuS_checker.conf
%post
chmod 600 /etc/KySKuS_checker.conf
chown root:root /etc/KySKuS_checker.conf
systemctl daemon-reload
%postun
if [ $1 -eq 0 ]; then
    systemctl --no-reload disable check.service >/dev/null 2>&1 || :
fi
