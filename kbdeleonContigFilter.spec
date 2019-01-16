/*
A KBase module: kbdeleonContigFilter
This sample module contains one small method that filters contigs.
*/

module kbdeleonContigFilter {
    typedef structure {
        string report_name;
        string report_ref;
    } ReportResults;

    /*
        This example function accepts any number of parameters and returns results in a KBaseReport
    */
    funcdef run_kbdeleonContigFilter(mapping<string,UnspecifiedObject> params) returns (ReportResults output) authentication required;
    funcdef run_kbdeleonContigFilter_max(mapping<string,UnspecifiedObject> params) returns (ReportResults output) authentication required;

};
