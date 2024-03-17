use std::fs;
use std::path::PathBuf;
use std::process::Command;

// hide root window
let root = Tk::root();
root.withdraw();
// hide root window
let root = Tk::root();
root.withdraw();

// Intro guide messagebox
showinfo("info", "Selecione onde será salva a task.");

// Shows dialog box and return the path
let path: String = askdirectory(initialdir = "C:\\Users\\RodrigoMC\\Desktop", title = "Pasta destino")?;
println!("{}", path);

// Creates the folder
let current_dir: PathBuf = fs::canonicalize(".")?.join(path);
if !current_dir.exists() {
    fs::create_dir(&current_dir)?;
}

// Asks the folder name
let userStr: String = simpledialog("Criar pasta", "Cole o título da task no Collab aqui.")?;

// Cleans the folder name
let cleanStr1: String = userStr.replace(":", "-");
let cleanStr2: String = cleanStr1.replace("/", "-");
let cleanStr3: String = cleanStr2.replace(".", "-");
let cleanStr4: String = cleanStr2.replace("|", "-");
let new_folder: String = format!("{}{}", userStr, "/00_materiais/01_layout/02_view");

// Tests if the folder a ready exists
if !current_dir.join(&new_folder).exists() {
    // Creates the subfolders
    let mut command = Command::new("mkdir")
        .arg("-p")
        .args(&[&new_folder])
        .current_dir(PathBuf::from(&current_dir));
    if !command.status()?.success() {
        eprintln!("{}", command);
        return;
    }

    // Success feedback
    showinfo("info", "Sucesso Total!");
} else {
    // Error feedback
    showinfo(
        "info",
        "Erro: A pasta já existe! \
                             Verifique o nome da task.",
    );
}

// Intro guide messagebox
showinfo("info", "Selecione onde será salva a task.");

// Shows dialog box and return the path
let path = askdirectory(initialdir = "C:\\Users\\RodrigoMC\\Desktop", title = "Pasta destino").unwrap();
println!("{}", path);

// Creates the folder
let current_dir: PathBuf = fs::canonicalize(".")?;
let new_path: PathBuf = current_dir.join(path);
if !new_path.exists() {
    fs::create_dir(&new_path)?;
}

// Asks the folder name
let userStr = simpledialog("Criar pasta", "Cole o título da task no Collab aqui.");

// Cleans the folder name
let cleanStr1 = userStr.replace(":", "-");
let cleanStr2 = cleanStr1.replace("/", "-");
let cleanStr3 = cleanStr2.replace(".", "-");
let cleanStr4 = cleanStr2.replace("|", "-");
let new_folder: String = format!("{}{}", userStr, "/00_materiais/01_layout/02_view");

// Tests if the folder a ready exists
if !new_path.join(&new_folder).exists() {
    // Creates the subfolders
    let mut command = Command::new("mkdir")
        .arg("-p")
        .args(&[&new_folder])
        .current_dir(PathBuf::from(&new_path));
    if !command.status()?.success() {
        eprintln!("{}", command);
        return;
    }

    // Success feedback
    showinfo("info", "Sucesso Total!");
} else {
    // Error feedback
    showinfo(
        "info",
        "Erro: A pasta já existe! \
                             Verifique o nome da task.",
    );
}
