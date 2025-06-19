### Difference calculator

### Hexlet tests and linter status:
[![Actions Status](https://github.com/INafanya/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/INafanya/python-project-50/actions)
[![Python CI](https://github.com/INafanya/python-project-50/actions/workflows/pyci.yaml/badge.svg)](https://github.com/INafanya/python-project-50/actions/workflows/pyci.yaml)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=INafanya_python-project-50&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=INafanya_python-project-50)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=INafanya_python-project-50&metric=coverage)](https://sonarcloud.io/summary/new_code?id=INafanya_python-project-50)

---

### **Project Overview**

It is a CLI tool that allows users to compare two configuration files (*.JSON* or *.YAML*) and output their differences in various formats:
- stylish
- plain
- json

---

### **Requirements**

- python 3.10+
- uv
  
---

### **Installation**

```
git clone git@github.com:INafanya/python-project-50.git
```
```
cd python-project-50
```
```
make build
```
```
make install
```

---

### **Usage**

To use the tool from the command line, run the following command:
```
gendiff <file_path1> <file_path2> --format <format>
```
Arguments:
- *```<file_path1>```* — path to first file;
- *```<file_path2>```* — path to second file;
- *```<format>```* — stylish(default)/plain/json.

For help run: 
```
gendiff -h
```

---

### **Usage Examples**

#### **Comparing two flat .json files:**

   [![asciicast](https://asciinema.org/a/0QB5LuDQVcOVcEL415QjyWt9y.svg)](https://asciinema.org/a/0QB5LuDQVcOVcEL415QjyWt9y)


#### **Comparing two flat .yaml files:**

   [![asciicast](https://asciinema.org/a/Dbz4vf54wk1B5l3kIfOzgTpvr.svg)](https://asciinema.org/a/Dbz4vf54wk1B5l3kIfOzgTpvr)


#### **Comparing two .json or .yaml files with a nested structure:**
   
   - #### Stylish Output Format:
   [![asciicast](https://asciinema.org/a/HYCVxIrPXzCie0ci2AYrlH5uw.svg)](https://asciinema.org/a/HYCVxIrPXzCie0ci2AYrlH5uw)

   
   - #### Plain Output Format:
   [![asciicast](https://asciinema.org/a/uGLyjP0B6awvEtPAXpPK3DDnS.svg)](https://asciinema.org/a/uGLyjP0B6awvEtPAXpPK3DDnS)

   
   - #### JSON Output Format:
   [![asciicast](https://asciinema.org/a/thuYXSGsxNlvoIoVvy15zVFRb.svg)](https://asciinema.org/a/thuYXSGsxNlvoIoVvy15zVFRb)
   
