package SequenceSetUtils::SequenceSetUtilsClient;

use JSON::RPC::Client;
use POSIX;
use strict;
use Data::Dumper;
use URI;
use Bio::KBase::Exceptions;
my $get_time = sub { time, 0 };
eval {
    require Time::HiRes;
    $get_time = sub { Time::HiRes::gettimeofday() };
};

use Bio::KBase::AuthToken;

# Client version should match Impl version
# This is a Semantic Version number,
# http://semver.org
our $VERSION = "0.1.0";

=head1 NAME

SequenceSetUtils::SequenceSetUtilsClient

=head1 DESCRIPTION


A KBase module: SequenceSetUtils


=cut

sub new
{
    my($class, $url, @args) = @_;
    

    my $self = {
	client => SequenceSetUtils::SequenceSetUtilsClient::RpcClient->new,
	url => $url,
	headers => [],
    };

    chomp($self->{hostname} = `hostname`);
    $self->{hostname} ||= 'unknown-host';

    #
    # Set up for propagating KBRPC_TAG and KBRPC_METADATA environment variables through
    # to invoked services. If these values are not set, we create a new tag
    # and a metadata field with basic information about the invoking script.
    #
    if ($ENV{KBRPC_TAG})
    {
	$self->{kbrpc_tag} = $ENV{KBRPC_TAG};
    }
    else
    {
	my ($t, $us) = &$get_time();
	$us = sprintf("%06d", $us);
	my $ts = strftime("%Y-%m-%dT%H:%M:%S.${us}Z", gmtime $t);
	$self->{kbrpc_tag} = "C:$0:$self->{hostname}:$$:$ts";
    }
    push(@{$self->{headers}}, 'Kbrpc-Tag', $self->{kbrpc_tag});

    if ($ENV{KBRPC_METADATA})
    {
	$self->{kbrpc_metadata} = $ENV{KBRPC_METADATA};
	push(@{$self->{headers}}, 'Kbrpc-Metadata', $self->{kbrpc_metadata});
    }

    if ($ENV{KBRPC_ERROR_DEST})
    {
	$self->{kbrpc_error_dest} = $ENV{KBRPC_ERROR_DEST};
	push(@{$self->{headers}}, 'Kbrpc-Errordest', $self->{kbrpc_error_dest});
    }

    #
    # This module requires authentication.
    #
    # We create an auth token, passing through the arguments that we were (hopefully) given.

    {
	my %arg_hash2 = @args;
	if (exists $arg_hash2{"token"}) {
	    $self->{token} = $arg_hash2{"token"};
	} elsif (exists $arg_hash2{"user_id"}) {
	    my $token = Bio::KBase::AuthToken->new(@args);
	    if (!$token->error_message) {
	        $self->{token} = $token->token;
	    }
	}
	
	if (exists $self->{token})
	{
	    $self->{client}->{token} = $self->{token};
	}
    }

    my $ua = $self->{client}->ua;	 
    my $timeout = $ENV{CDMI_TIMEOUT} || (30 * 60);	 
    $ua->timeout($timeout);
    bless $self, $class;
    #    $self->_validate_version();
    return $self;
}




=head2 buildFromFasta

  $out = $obj->buildFromFasta($params)

=over 4

=item Parameter and return types

=begin html

<pre>
$params is a SequenceSetUtils.FastaInputParams
$out is a SequenceSetUtils.SequenceSetOutputParams
FastaInputParams is a reference to a hash where the following keys are defined:
	ws_name has a value which is a string
	path has a value which is a string
SequenceSetOutputParams is a reference to a hash where the following keys are defined:
	SequenceSet_ref has a value which is a string

</pre>

=end html

=begin text

$params is a SequenceSetUtils.FastaInputParams
$out is a SequenceSetUtils.SequenceSetOutputParams
FastaInputParams is a reference to a hash where the following keys are defined:
	ws_name has a value which is a string
	path has a value which is a string
SequenceSetOutputParams is a reference to a hash where the following keys are defined:
	SequenceSet_ref has a value which is a string


=end text

=item Description



=back

=cut

 sub buildFromFasta
{
    my($self, @args) = @_;

# Authentication: required

    if ((my $n = @args) != 1)
    {
	Bio::KBase::Exceptions::ArgumentValidationError->throw(error =>
							       "Invalid argument count for function buildFromFasta (received $n, expecting 1)");
    }
    {
	my($params) = @args;

	my @_bad_arguments;
        (ref($params) eq 'HASH') or push(@_bad_arguments, "Invalid type for argument 1 \"params\" (value was \"$params\")");
        if (@_bad_arguments) {
	    my $msg = "Invalid arguments passed to buildFromFasta:\n" . join("", map { "\t$_\n" } @_bad_arguments);
	    Bio::KBase::Exceptions::ArgumentValidationError->throw(error => $msg,
								   method_name => 'buildFromFasta');
	}
    }

    my $url = $self->{url};
    my $result = $self->{client}->call($url, $self->{headers}, {
	    method => "SequenceSetUtils.buildFromFasta",
	    params => \@args,
    });
    if ($result) {
	if ($result->is_error) {
	    Bio::KBase::Exceptions::JSONRPC->throw(error => $result->error_message,
					       code => $result->content->{error}->{code},
					       method_name => 'buildFromFasta',
					       data => $result->content->{error}->{error} # JSON::RPC::ReturnObject only supports JSONRPC 1.1 or 1.O
					      );
	} else {
	    return wantarray ? @{$result->result} : $result->result->[0];
	}
    } else {
        Bio::KBase::Exceptions::HTTP->throw(error => "Error invoking method buildFromFasta",
					    status_line => $self->{client}->status_line,
					    method_name => 'buildFromFasta',
				       );
    }
}
 


=head2 buildFromLocations

  $out = $obj->buildFromLocations($params)

=over 4

=item Parameter and return types

=begin html

<pre>
$params is a SequenceSetUtils.LocationInputParams
$out is a SequenceSetUtils.SequenceSetOutputParams
LocationInputParams is a reference to a hash where the following keys are defined:
	ws_name has a value which is a string
	seqlocations has a value which is a reference to a list where each element is a SequenceSetUtils.sequence_location
sequence_location is a reference to a hash where the following keys are defined:
	genome_ref has a value which is a string
	genlocations has a value which is a reference to a list where each element is a reference to a list containing 4 items:
		0: a SequenceSetUtils.Contig_id
		1: an int
		2: a SequenceSetUtils.orientation
		3: an int

Contig_id is a string
orientation is a string
SequenceSetOutputParams is a reference to a hash where the following keys are defined:
	SequenceSet_ref has a value which is a string

</pre>

=end html

=begin text

$params is a SequenceSetUtils.LocationInputParams
$out is a SequenceSetUtils.SequenceSetOutputParams
LocationInputParams is a reference to a hash where the following keys are defined:
	ws_name has a value which is a string
	seqlocations has a value which is a reference to a list where each element is a SequenceSetUtils.sequence_location
sequence_location is a reference to a hash where the following keys are defined:
	genome_ref has a value which is a string
	genlocations has a value which is a reference to a list where each element is a reference to a list containing 4 items:
		0: a SequenceSetUtils.Contig_id
		1: an int
		2: a SequenceSetUtils.orientation
		3: an int

Contig_id is a string
orientation is a string
SequenceSetOutputParams is a reference to a hash where the following keys are defined:
	SequenceSet_ref has a value which is a string


=end text

=item Description



=back

=cut

 sub buildFromLocations
{
    my($self, @args) = @_;

# Authentication: required

    if ((my $n = @args) != 1)
    {
	Bio::KBase::Exceptions::ArgumentValidationError->throw(error =>
							       "Invalid argument count for function buildFromLocations (received $n, expecting 1)");
    }
    {
	my($params) = @args;

	my @_bad_arguments;
        (ref($params) eq 'HASH') or push(@_bad_arguments, "Invalid type for argument 1 \"params\" (value was \"$params\")");
        if (@_bad_arguments) {
	    my $msg = "Invalid arguments passed to buildFromLocations:\n" . join("", map { "\t$_\n" } @_bad_arguments);
	    Bio::KBase::Exceptions::ArgumentValidationError->throw(error => $msg,
								   method_name => 'buildFromLocations');
	}
    }

    my $url = $self->{url};
    my $result = $self->{client}->call($url, $self->{headers}, {
	    method => "SequenceSetUtils.buildFromLocations",
	    params => \@args,
    });
    if ($result) {
	if ($result->is_error) {
	    Bio::KBase::Exceptions::JSONRPC->throw(error => $result->error_message,
					       code => $result->content->{error}->{code},
					       method_name => 'buildFromLocations',
					       data => $result->content->{error}->{error} # JSON::RPC::ReturnObject only supports JSONRPC 1.1 or 1.O
					      );
	} else {
	    return wantarray ? @{$result->result} : $result->result->[0];
	}
    } else {
        Bio::KBase::Exceptions::HTTP->throw(error => "Error invoking method buildFromLocations",
					    status_line => $self->{client}->status_line,
					    method_name => 'buildFromLocations',
				       );
    }
}
 


=head2 buildFromFeatureSet

  $out = $obj->buildFromFeatureSet($params)

=over 4

=item Parameter and return types

=begin html

<pre>
$params is a SequenceSetUtils.FeatureSetInputParams
$out is a SequenceSetUtils.SequenceSetOutputParams
FeatureSetInputParams is a reference to a hash where the following keys are defined:
	ws_name has a value which is a string
	FeatureSet_ref has a value which is a string
	genome_ref has a value which is a string
	upstream_length has a value which is an int
SequenceSetOutputParams is a reference to a hash where the following keys are defined:
	SequenceSet_ref has a value which is a string

</pre>

=end html

=begin text

$params is a SequenceSetUtils.FeatureSetInputParams
$out is a SequenceSetUtils.SequenceSetOutputParams
FeatureSetInputParams is a reference to a hash where the following keys are defined:
	ws_name has a value which is a string
	FeatureSet_ref has a value which is a string
	genome_ref has a value which is a string
	upstream_length has a value which is an int
SequenceSetOutputParams is a reference to a hash where the following keys are defined:
	SequenceSet_ref has a value which is a string


=end text

=item Description



=back

=cut

 sub buildFromFeatureSet
{
    my($self, @args) = @_;

# Authentication: required

    if ((my $n = @args) != 1)
    {
	Bio::KBase::Exceptions::ArgumentValidationError->throw(error =>
							       "Invalid argument count for function buildFromFeatureSet (received $n, expecting 1)");
    }
    {
	my($params) = @args;

	my @_bad_arguments;
        (ref($params) eq 'HASH') or push(@_bad_arguments, "Invalid type for argument 1 \"params\" (value was \"$params\")");
        if (@_bad_arguments) {
	    my $msg = "Invalid arguments passed to buildFromFeatureSet:\n" . join("", map { "\t$_\n" } @_bad_arguments);
	    Bio::KBase::Exceptions::ArgumentValidationError->throw(error => $msg,
								   method_name => 'buildFromFeatureSet');
	}
    }

    my $url = $self->{url};
    my $result = $self->{client}->call($url, $self->{headers}, {
	    method => "SequenceSetUtils.buildFromFeatureSet",
	    params => \@args,
    });
    if ($result) {
	if ($result->is_error) {
	    Bio::KBase::Exceptions::JSONRPC->throw(error => $result->error_message,
					       code => $result->content->{error}->{code},
					       method_name => 'buildFromFeatureSet',
					       data => $result->content->{error}->{error} # JSON::RPC::ReturnObject only supports JSONRPC 1.1 or 1.O
					      );
	} else {
	    return wantarray ? @{$result->result} : $result->result->[0];
	}
    } else {
        Bio::KBase::Exceptions::HTTP->throw(error => "Error invoking method buildFromFeatureSet",
					    status_line => $self->{client}->status_line,
					    method_name => 'buildFromFeatureSet',
				       );
    }
}
 
  
sub status
{
    my($self, @args) = @_;
    if ((my $n = @args) != 0) {
        Bio::KBase::Exceptions::ArgumentValidationError->throw(error =>
                                   "Invalid argument count for function status (received $n, expecting 0)");
    }
    my $url = $self->{url};
    my $result = $self->{client}->call($url, $self->{headers}, {
        method => "SequenceSetUtils.status",
        params => \@args,
    });
    if ($result) {
        if ($result->is_error) {
            Bio::KBase::Exceptions::JSONRPC->throw(error => $result->error_message,
                           code => $result->content->{error}->{code},
                           method_name => 'status',
                           data => $result->content->{error}->{error} # JSON::RPC::ReturnObject only supports JSONRPC 1.1 or 1.O
                          );
        } else {
            return wantarray ? @{$result->result} : $result->result->[0];
        }
    } else {
        Bio::KBase::Exceptions::HTTP->throw(error => "Error invoking method status",
                        status_line => $self->{client}->status_line,
                        method_name => 'status',
                       );
    }
}
   

sub version {
    my ($self) = @_;
    my $result = $self->{client}->call($self->{url}, $self->{headers}, {
        method => "SequenceSetUtils.version",
        params => [],
    });
    if ($result) {
        if ($result->is_error) {
            Bio::KBase::Exceptions::JSONRPC->throw(
                error => $result->error_message,
                code => $result->content->{code},
                method_name => 'buildFromFeatureSet',
            );
        } else {
            return wantarray ? @{$result->result} : $result->result->[0];
        }
    } else {
        Bio::KBase::Exceptions::HTTP->throw(
            error => "Error invoking method buildFromFeatureSet",
            status_line => $self->{client}->status_line,
            method_name => 'buildFromFeatureSet',
        );
    }
}

sub _validate_version {
    my ($self) = @_;
    my $svr_version = $self->version();
    my $client_version = $VERSION;
    my ($cMajor, $cMinor) = split(/\./, $client_version);
    my ($sMajor, $sMinor) = split(/\./, $svr_version);
    if ($sMajor != $cMajor) {
        Bio::KBase::Exceptions::ClientServerIncompatible->throw(
            error => "Major version numbers differ.",
            server_version => $svr_version,
            client_version => $client_version
        );
    }
    if ($sMinor < $cMinor) {
        Bio::KBase::Exceptions::ClientServerIncompatible->throw(
            error => "Client minor version greater than Server minor version.",
            server_version => $svr_version,
            client_version => $client_version
        );
    }
    if ($sMinor > $cMinor) {
        warn "New client version available for SequenceSetUtils::SequenceSetUtilsClient\n";
    }
    if ($sMajor == 0) {
        warn "SequenceSetUtils::SequenceSetUtilsClient version is $svr_version. API subject to change.\n";
    }
}

=head1 TYPES



=head2 Contig_id

=over 4



=item Description

Insert your typespec information here.


=item Definition

=begin html

<pre>
a string
</pre>

=end html

=begin text

a string

=end text

=back



=head2 orientation

=over 4



=item Definition

=begin html

<pre>
a string
</pre>

=end html

=begin text

a string

=end text

=back



=head2 sequence_location

=over 4



=item Description

genome_ref - handle to genome
genlocations - list of locations in the genome to build a single sequence from, usually length 1


=item Definition

=begin html

<pre>
a reference to a hash where the following keys are defined:
genome_ref has a value which is a string
genlocations has a value which is a reference to a list where each element is a reference to a list containing 4 items:
	0: a SequenceSetUtils.Contig_id
	1: an int
	2: a SequenceSetUtils.orientation
	3: an int


</pre>

=end html

=begin text

a reference to a hash where the following keys are defined:
genome_ref has a value which is a string
genlocations has a value which is a reference to a list where each element is a reference to a list containing 4 items:
	0: a SequenceSetUtils.Contig_id
	1: an int
	2: a SequenceSetUtils.orientation
	3: an int



=end text

=back



=head2 FastaInputParams

=over 4



=item Description

ws_name - workspace name
path - path to fasta in the workspace


=item Definition

=begin html

<pre>
a reference to a hash where the following keys are defined:
ws_name has a value which is a string
path has a value which is a string

</pre>

=end html

=begin text

a reference to a hash where the following keys are defined:
ws_name has a value which is a string
path has a value which is a string


=end text

=back



=head2 LocationInputParams

=over 4



=item Description

ws_name - workspace name
seqlocations - list of sequence locations


=item Definition

=begin html

<pre>
a reference to a hash where the following keys are defined:
ws_name has a value which is a string
seqlocations has a value which is a reference to a list where each element is a SequenceSetUtils.sequence_location

</pre>

=end html

=begin text

a reference to a hash where the following keys are defined:
ws_name has a value which is a string
seqlocations has a value which is a reference to a list where each element is a SequenceSetUtils.sequence_location


=end text

=back



=head2 FeatureSetInputParams

=over 4



=item Description

ws_name - workspace name
FeatureSet_ref - handle to input feature set
genome_ref - handle to genome to extract features from
upstream_length - length of region upstream of features to extract sequences from


=item Definition

=begin html

<pre>
a reference to a hash where the following keys are defined:
ws_name has a value which is a string
FeatureSet_ref has a value which is a string
genome_ref has a value which is a string
upstream_length has a value which is an int

</pre>

=end html

=begin text

a reference to a hash where the following keys are defined:
ws_name has a value which is a string
FeatureSet_ref has a value which is a string
genome_ref has a value which is a string
upstream_length has a value which is an int


=end text

=back



=head2 SequenceSetOutputParams

=over 4



=item Description

SequenceSet_ref - handle to the new SequenceSet object


=item Definition

=begin html

<pre>
a reference to a hash where the following keys are defined:
SequenceSet_ref has a value which is a string

</pre>

=end html

=begin text

a reference to a hash where the following keys are defined:
SequenceSet_ref has a value which is a string


=end text

=back



=cut

package SequenceSetUtils::SequenceSetUtilsClient::RpcClient;
use base 'JSON::RPC::Client';
use POSIX;
use strict;

#
# Override JSON::RPC::Client::call because it doesn't handle error returns properly.
#

sub call {
    my ($self, $uri, $headers, $obj) = @_;
    my $result;


    {
	if ($uri =~ /\?/) {
	    $result = $self->_get($uri);
	}
	else {
	    Carp::croak "not hashref." unless (ref $obj eq 'HASH');
	    $result = $self->_post($uri, $headers, $obj);
	}

    }

    my $service = $obj->{method} =~ /^system\./ if ( $obj );

    $self->status_line($result->status_line);

    if ($result->is_success) {

        return unless($result->content); # notification?

        if ($service) {
            return JSON::RPC::ServiceObject->new($result, $self->json);
        }

        return JSON::RPC::ReturnObject->new($result, $self->json);
    }
    elsif ($result->content_type eq 'application/json')
    {
        return JSON::RPC::ReturnObject->new($result, $self->json);
    }
    else {
        return;
    }
}


sub _post {
    my ($self, $uri, $headers, $obj) = @_;
    my $json = $self->json;

    $obj->{version} ||= $self->{version} || '1.1';

    if ($obj->{version} eq '1.0') {
        delete $obj->{version};
        if (exists $obj->{id}) {
            $self->id($obj->{id}) if ($obj->{id}); # if undef, it is notification.
        }
        else {
            $obj->{id} = $self->id || ($self->id('JSON::RPC::Client'));
        }
    }
    else {
        # $obj->{id} = $self->id if (defined $self->id);
	# Assign a random number to the id if one hasn't been set
	$obj->{id} = (defined $self->id) ? $self->id : substr(rand(),2);
    }

    my $content = $json->encode($obj);

    $self->ua->post(
        $uri,
        Content_Type   => $self->{content_type},
        Content        => $content,
        Accept         => 'application/json',
	@$headers,
	($self->{token} ? (Authorization => $self->{token}) : ()),
    );
}



1;
