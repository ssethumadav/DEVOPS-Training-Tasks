def logFile = new File('/var/log/apache2/access.log.1')  // Ensure the path is correct
def regex = /\[([^\]]+)\]\s+"(\w+)\s([^\s"]*)\s?HTTP\/[0-9.]+\"\s(\d{3})\s(\d+)\s+"([^"]*)"/

def errorCount = 0
def requestCount = [:]
def invalidCount = 0
def statusCounts = [:]
println "Parsing the log file..."

logFile.eachLine { line ->
    def matcher = line =~ regex
    if (matcher.find()) {
//	println "Matched: ${matcher.group(0)}"
//	println "Match found!"
        def timestamp = matcher[0][1]
        def method = matcher[0][2]
        def request = matcher[0][3]
        def statusCode = matcher[0][4]
        def responseSize = matcher[0][5]
        def userAgent = matcher[0][6]

        // Count errors
        if (statusCode.startsWith('4') || statusCode.startsWith('5')) {
            errorCount++
        }

        requestCount[method] = (requestCount[method] ?: 0) + 1

        statusCounts[statusCode] = (statusCounts[statusCode] ?: 0) + 1
    } else {
	invalidCount++
        println "..." // If the regex doesn't match, print the line
    }
}
println "Log report has been generated"

def report = """
Log Analysis Report
===================
Total Errors: $errorCount
Invalid Requests: $invalidCount
Request Counts: $requestCount
Status Code Counts: $statusCounts
"""

new File('log_report.txt').text = report

