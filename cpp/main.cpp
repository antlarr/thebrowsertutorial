#include "mainwindow.h"
#include <QApplication>
#include <QTranslator>
#include <QDebug>

int main(int argc, char *argv[])
{
    QApplication app(argc, argv);

    QString locale_name = QLocale::system().name();
    QString filename = "thebrowser." + locale_name;
    QString languages_directory = app.applicationDirPath() + "/../cpp/languages/";
    QTranslator translator;
    if (!translator.load(filename, languages_directory))
    {
        qDebug() << QString("The language file wasn't found in %1 . "
                            "Please adjust the sources to search for the translation files"
                            "in the right directory or add a translation for %2")
                    .arg(languages_directory)
                    .arg(locale_name);
    }
    app.installTranslator(&translator);

    MainWindow w;
    w.show();

    return app.exec();
}
