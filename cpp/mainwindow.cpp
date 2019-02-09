#include "mainwindow.h"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    QMenuBar *menubar = menuBar();

    QMenu *menu = menubar->addMenu(tr("File"));
    auto action = new QAction(tr("Quit"), this);
    action->setIcon(QIcon::fromTheme("application-exit"));
    connect(action, &QAction::triggered, qApp, &QApplication::quit);

    menu->addAction(action);
    ui->mainToolBar->addAction(action);
}


MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::loadLocation()
{
    QUrl url = ui->lineEdit->text();
    if (url.scheme().isEmpty())
        url.setScheme("https");
    ui->webView->load(url);
}

void MainWindow::urlChanged(const QUrl &url)
{
    ui->lineEdit->setText(url.toString());
}

