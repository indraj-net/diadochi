# diadochi.py -- The Diadochi Static Site Generator
# Copyright (C) 2025 Indraj Gandham <hello@indraj.net>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


import os
import shutil
import time


VERSION = 1
REVISION = 1


if __name__ == "__main__":

	print(
		f"The Diadochi Static Site Generator, v{VERSION} rev{REVISION}\n"
		"Copyright (C) 2025 Indraj Gandham\n"
		"This software comes with ABSOLUTELY NO WARRANTY; "
		"see COPYING for details.\n")

	start_time = time.perf_counter()

	print("Clearing output directory...")

	if os.path.exists("out"):
		shutil.rmtree("out")

	os.makedirs("out")

	print("Reading header and footer...")

	with open("config/header.html", "r") as file:
		header = file.read()
	with open("config/footer.html", "r") as file:
		footer = file.read()

	for root, dirs, files in os.walk("pages"):

		rel_dir = os.path.relpath(root, "pages")

		if rel_dir == '.':
			target_dir = "out"
		else:
			target_dir = os.path.join("out", rel_dir)

		if rel_dir != '.':
			print(f"Creating {rel_dir}...")
			os.makedirs(target_dir)

		for file in files:

			if rel_dir == '.':
				rel_filepath = file
			else:
				rel_filepath = os.path.join(rel_dir, file)

			src_file = os.path.join("pages", rel_filepath)
			out_file = os.path.join("out", rel_filepath)

			if file == "index.html":
				print(f"Processing {rel_filepath}...")
				with open(src_file, "r") as file_d:
					content = file_d.read()
				with open(out_file, "w") as file_d:
					file_d.write(header)
					file_d.write(content)
					file_d.write(footer)
			else:
				print(f"Copying {rel_filepath}...")
				shutil.copy2(src_file, out_file)

	elapsed_time = time.perf_counter() - start_time
	print(f"\nBuild finished in {elapsed_time:.2f} s")
