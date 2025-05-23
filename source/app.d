/*
 * app.d -- The Diadochi Static Site Generator
 * Copyright (C) 2025 Indraj Gandham <hello@indraj.net>
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU Affero General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU Affero General Public License for more details.
 *
 * You should have received a copy of the GNU Affero General Public License
 * along with this program.  If not, see <https://www.gnu.org/licenses/>.
 */


import std.stdio;
import std.file;
import std.path;
import std.string;
import std.datetime.stopwatch;
import std.parallelism;


void processFile(string srcPath, string destPath, string header, string footer)
{
	mkdirRecurse(dirName(destPath));
	if (srcPath.baseName == "index.html" ||
		srcPath.baseName == "not_found.html") {

		writefln("Processing %s...", srcPath);
		string content = readText(srcPath);
		std.file.write(destPath, header ~ content ~ footer);

	} else {
		writefln("Copying %s...", srcPath);
		copy(srcPath, destPath);
	}
}


void main()
{
	writeln("The Diadochi Static Site Generator, v2.0.0\n"
		~ "Copyright (C) 2025 Indraj Gandham\n"
		~ "This software comes with ABSOLUTELY NO WARRANTY; "
		~ "see COPYING for details.\n");

	writeln("Clearing output directory...");
	if ("out".exists) {
		rmdirRecurse("out");
	}
	mkdir("out");

	writeln("Reading header and footer...");
	string header = readText("config/header.html");
	string footer = readText("config/footer.html");

	TaskPool pool = taskPool();
	writefln("\nUsing %d threads.\n", defaultPoolThreads);

	StopWatch timer;
	timer.start();

	foreach (DirEntry entry; dirEntries("pages", SpanMode.depth)) {
		string destPath = buildPath("out", chompPrefix(entry.name,
							"pages/"));
		if (entry.isFile) {
			pool.put(task(&processFile, entry.name, destPath,
					header, footer));
		}
	}

	pool.finish(true);
	timer.stop();

	writefln("\nBuilt successfully in %.3f s",
		(cast(double) timer.peek.total!"msecs") / 1000);
}
